from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from djutil.models import TimeStampedModel
from django.contrib.auth.models import AbstractBaseUser, User

class User(AbstractBaseUser, TimeStampedModel):
    first_name = models.CharField(_('first name'), max_length=254, blank=True, default="")
    middle_name = models.CharField(_('middle name'), max_length=254, blank=True, default="")
    last_name = models.CharField(_('last_name name'), max_length=254, blank=True, default="")
    gender = models.CharField(_('gender'), max_length=10, blank=True, default="")
    image = models.CharField(_('image'), max_length=1000, blank=True, default="")
    hometown = models.CharField(_('hometown'), max_length=254, blank=True, default="")
    email = models.EmailField(_('email address'), max_length=254, unique=True, primary_key=True)
    access_token = models.CharField(max_length=15000)
    facebook_id = models.BigIntegerField()
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-modified_at',]

class HobbyGroup(TimeStampedModel):
    hobby_id = models.AutoField(primary_key=True)
    hobby_name = models.CharField(max_length=50, blank=True)

class HobbyGroupUser(TimeStampedModel):
    hobby_group_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    hobby = models.ForeignKey(HobbyGroup)
