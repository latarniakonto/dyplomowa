from django.db.models.signals import pre_save, pre_delete
from django.db.models import Q
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from assets.models import (
    Asset,
    get_asset_initial_weight,
    get_asset_current_weight,
    update_assets_weight,
    update_asset_portfolio,
    update_asset,
)
from transactions.models import Transaction, Types


@receiver(pre_save, sender=Asset)
def add_slug_to_asset(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify('asset')
        instance.slug = slug + '-' + get_random_string(length=7)


@receiver(pre_save, sender=Transaction)
def update_or_create_asset_on_transaction_post(sender, instance, *args, **kwargs):
    if (
        instance.type == Types.BUY
        and instance.portfolio.cash < instance.value + instance.provision
    ):
        raise Exception

    asset, created = Asset.objects.get_or_create(
        ticker=instance.ticker, portfolio=instance.portfolio
    )

    if created and instance.type == Types.SELL and asset.total == 0:
        asset.delete()
        raise Exception

    elif instance.type == Types.SELL and asset.total < instance.amount:
        raise Exception

    update_asset(asset, instance)
    update_asset_portfolio(asset, instance)

    update_assets_weight()


@receiver(pre_delete, sender=Transaction)
def update_asset_on_transaction_delete(sender, instance, *args, **kwargs):
    asset = Asset.objects.get(ticker=instance.ticker, portfolio=instance.portfolio)

    update_asset(asset, instance, True)
    update_asset_portfolio(asset, instance, True)

    transactions = Transaction.objects.all()
    if not transactions.filter(~Q(uutid=instance.uutid), ticker=asset.ticker).exists():
        asset.delete()

    update_assets_weight()
