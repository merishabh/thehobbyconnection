from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', UserPost.as_view(), name='user_post'),
]
