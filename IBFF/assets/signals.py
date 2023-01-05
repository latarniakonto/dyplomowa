import datetime
from django.db.models.signals import pre_save, pre_delete
from django.db.models import Q
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from assets.models import Asset
from snapshots.models import Snapshot


@receiver(pre_save, sender=Asset)
def add_slug_to_asset(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify('asset')
        instance.slug = slug + '-' + get_random_string(length=7)


@receiver(pre_delete, sender=Asset)
def on_dividend_cascade_delete(sender, instance, *args, **kwargs):
    portfolio = instance.portfolio
    for dividend in instance.dividends.all():
        portfolio.cash -= dividend.value
        portfolio.value -= dividend.value
        portfolio.annual_dividends -= dividend.value

        today = datetime.date.today()
        try:
            snapshot = Snapshot.objects.get(
                portfolio=portfolio, date__year=today.year - 1
            )
            portfolio.annual_gain = portfolio.value - snapshot.value
            portfolio.annual_yield = portfolio.value / snapshot.value - 1

        except Snapshot.DoesNotExist:
            portfolio.annual_gain = portfolio.value - portfolio.deposit
            portfolio.annual_yield = portfolio.value / portfolio.deposit - 1

    portfolio.save()
