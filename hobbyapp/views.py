import urllib
import pdb
import requests

from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import Http404, HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from theHobbyConnection import settings
from django.contrib.auth import authenticate, login

class Login(APIView):

    def get(self, request):
        args = {
            'client_id': settings.SOCIAL_AUTH_FACEBOOK_KEY,
            'scope': settings.FACEBOOK_SCOPE,
            'redirect_uri': request.build_absolute_uri('/authentication_callback'),
        }
        # req = requests.get('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))
        return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))


class AuthenticationCallback(APIView):

    def get(self, request):
        code = request.GET.get('code')
        user = authenticate(token=code, request=request)

        if user.is_anonymous():
            url = reverse('facebook_setup')
            url += "?code=%s" % code

            resp = HttpResponseRedirect(url)

        else:
            login(request, user)

            url = getattr(settings, "LOGIN_REDIRECT_URL", "/home/")

            resp = HttpResponseRedirect(url)
        
        return resp

