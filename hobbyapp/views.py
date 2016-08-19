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
from hobbyapp.serializers import *
from hobbyapp import models as hobbyapp_models

class Login(APIView):

    def post(self, request):
        try:
            fb_user = hobbyapp_models.User.objects.get(facebook_id=request.data.get('facebook_id'))
            fb_user.access_token = request.data.get('access_token')
            fb_user.image = request.data.get('image')
            fb_user.save()
        except User.DoesNotExist:
            fb_user = hobbyapp_models.User.objects.create(**request.data)
        return Response("Success", status=status.HTTP_201_CREATED)



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
