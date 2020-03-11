from datetime import datetime

from django.contrib.postgres.search import SearchVector
from django.db import models
from django.db.models import Q
from six import python_2_unicode_compatible
import feed.models.Exercise


@python_2_unicode_compatible
class User(models.Model):
    userName = models.CharField(
        max_length=50,
        verbose_name='Username'
    )
    email = models.CharField(
        max_length=100,
        verbose_name='Email'
    )
    age = models.IntegerField(
        default=0,
        verbose_name='Age'
    )
    password = models.CharField(
        max_length=32,
        widget=forms.PasswordInput
    )
    sex = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    pro = models.BooleanField(
        default=false,
        verbose_name='Profesjonell bruker'
    )
    hasLiked = models.ManyToManyField(
        Exercise,
        blank=True,
        verbose_name='Liked Exercises'
    )
    # make this field read-only for normal users
    hasRated = models.ManyToManyField(
        Exercise,
        blank=true,
        verbose_name='Ranked Exercises'
    )

    class Meta(object):
        ordering = ["userName", "email", "age", "password", "sex"]

    def __str__(self):
        return self.userName
