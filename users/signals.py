# This file will create a profile while a user registers to the site

from django.db.models.signals import post_save
from django.contrib.auth.models import User  # The User model is going to be the sender
from django.dispatch import receiver  # A reciever is going to be a function that gets this signals and performs some tasks
from . models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
