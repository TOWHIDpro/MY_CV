from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from . models import user_profile


@receiver(post_save, sender=User)
def user_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        user_profile.objects.create(user=instance)

