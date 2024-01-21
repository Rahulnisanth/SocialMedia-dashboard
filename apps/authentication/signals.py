from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.contrib.auth.models import User
from .models import *


# SIGNALS
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            email=user.email,
        )


@receiver(post_save, sender=Profile)
def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user = profile.user
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
