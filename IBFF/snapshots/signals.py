from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from snapshots.models import Snapshot


@receiver(pre_save, sender=Snapshot)
def add_slug_to_asset(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify('snapshot')
        instance.slug = slug + '-' + get_random_string(length=7)
