from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from portfolios.models import Portfolio

@receiver(pre_save, sender=Portfolio)
def add_slug_to_portfolio(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.name)
        instance.slug = slug + "-" + get_random_string(length=7)
