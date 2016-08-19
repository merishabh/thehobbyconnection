from __future__ import unicode_literals

from django.db import models
from hobbyapp.models import *
from django.utils.translation import ugettext_lazy as _
from djutil.models import TimeStampedModel

class UserPost(TimeStampedModel):
    connected_user = models.ForeignKey(User)
    first_name = models.CharField(_('first name'), max_length=254, blank=True, default="")
    middle_name = models.CharField(_('middle name'), max_length=254, blank=True, default="")
    last_name = models.CharField(_('last_name name'), max_length=254, blank=True, default="")
    image = models.CharField(_('image'), max_length=1000, blank=True, default="")
    user_post = models.TextField()

    class Meta:
        ordering = ['-modified_at',]
