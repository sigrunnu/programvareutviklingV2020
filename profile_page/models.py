import sys

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

sys.path.append('/64/feed/models')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isPro = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CreatedBy(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username
