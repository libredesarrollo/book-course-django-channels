
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Alert

@receiver(post_save, sender=Alert)
def save_alert(sender, instance, **kwargs):
    print('Alert Created')