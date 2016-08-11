from __future__ import unicode_literals

from django.db import models
from hobbyapp.models import *
from djutil.models import TimeStampedModel

class UserPost(TimeStampedModel):
    connected_user = models.ForeignKey(User)
    user_post = models.TextField()
