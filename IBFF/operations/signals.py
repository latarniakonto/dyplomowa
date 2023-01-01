from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from operations.models import Dividend


@receiver(pre_save, sender=Dividend)
def add_slug_to_dividend(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify('dividend')
        instance.slug = slug + '-' + get_random_string(length=7)
