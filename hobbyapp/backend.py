import cgi, urllib, json

from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from django.db import IntegrityError

from hobbyapp.models import User

class FacebookBackend:
    def authenticate(self, token=None, request=None):

        args = {
            'client_id': settings.SOCIAL_AUTH_FACEBOOK_KEY,
            'client_secret': settings.SOCIAL_AUTH_FACEBOOK_SECRET,
            'redirect_uri': request.build_absolute_uri('/login/authentication_callback'),
            'code': token,
        }

        target = urllib.urlopen('https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(args)).read()
        response = cgi.parse_qs(target)
        access_token = response['access_token'][-1]


        fb_profile = urllib.urlopen('https://graph.facebook.com/me?locale=en_US&fields=name,email&access_token=%s' % access_token)
        fb_profile = json.load(fb_profile)

        user_data = {
                    'email': fb_profile.get('email'),
                    'access_token': access_token,
                    'facebook_id': fb_profile.get('id'),
        }
        try:

            fb_user = User.objects.get(facebook_id=fb_profile['id'])
            fb_user.access_token = user_data['access_token']
            fb_user.save()

        except User.DoesNotExist:

            fb_user = User.objects.create(**user_data)
        return fb_user

    def get_user(self, user_id):
        """ Just returns the user of a given ID. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    supports_object_permissions = False
    supports_anonymous_user = True
