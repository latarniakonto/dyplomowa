from django.db.models.signals import pre_save
from django.db.models import Q
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from assets.models import Asset


@receiver(pre_save, sender=Asset)
def add_slug_to_asset(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify('asset')
        instance.slug = slug + '-' + get_random_string(length=7)
