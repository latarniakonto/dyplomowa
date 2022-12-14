from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from transactions.models import Transaction

@receiver(pre_save, sender=Transaction)
def add_slug_to_transaction(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify('transaction')
        instance.slug = slug + '-' + get_random_string(length=7)
