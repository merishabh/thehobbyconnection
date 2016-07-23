from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from djutil.models import TimeStampedModel
from django.contrib.auth.models import AbstractBaseUser, User

class User(AbstractBaseUser, TimeStampedModel):
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    access_token = models.CharField(max_length=150)
    facebook_id = models.BigIntegerField()
    USERNAME_FIELD = 'email'


class HobbyGroup(TimeStampedModel):
    hobby_id = models.AutoField(primary_key=True)
    hobby_name = models.CharField(max_length=50, blank=True)

class HobbyGroupUser(TimeStampedModel):
    hobby_group_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    hobby = models.ForeignKey(HobbyGroup)





