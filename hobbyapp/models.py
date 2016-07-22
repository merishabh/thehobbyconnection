from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    USERNAME_FIELD = 'email'

class HobbyGroup(models.Model):
    hobby_id = models.AutoField(primary_key=True)
    hobby_name = models.CharField(max_length=50, blank=True)

class HobbyGroupUser(models.Model):
    hobby_group_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    hobby = models.ForeignKey(HobbyGroup)





