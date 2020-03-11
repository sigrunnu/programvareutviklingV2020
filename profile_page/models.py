from datetime import datetime

from django.contrib.postgres.search import SearchVector
from django.db import models
from django.db.models import Q
from six import python_2_unicode_compatible



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
    password = models.CharField(
        max_length=32,
        #widget=forms.PasswordInput
        verbose_name='Password'
    )
    pro = models.BooleanField(
        default=False,
        verbose_name='Profesjonell bruker'
    )
    hasLiked = models.ManyToManyField(
        to='feed.Exercise',
        blank=True,
        related_name='hasLiked',
        verbose_name='Liked Exercises'
    )

    class Meta(object):
        ordering = ["userName", "email", "password", "pro"]

    def __str__(self):
        return self.userName
