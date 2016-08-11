from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^authentication_callback/', AuthenticationCallback.as_view(), name='login_callback'),
    url(r'^$', Login.as_view(), name='login')
]
