import urllib
import pdb
import requests
import logging

from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import Http404, HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from theHobbyConnection import settings
from hobbyapp import models as hobbyapp_models
from UserPost.serializers import *

logger = logging.getLogger(__name__)

class UserPost(APIView):

    def post(self, request):
        try:
            import pdb; pdb.set_trace();
            access_token = request.META.get('HTTP_AUTHORIZATION').split(' ', 1)[1]
            user = hobbyapp_models.User.objects.get(access_token = access_token)
            request_data = {
                'user_post': request.data.get('post')
            }
            serializer = UserPostSerializer(data=request_data)
            serializer.initial_data['connected_user'] = user.email
            if serializer.is_valid():
                userPost_obj = serializer.save()
            else:
                return Response(dict(serializer.errors.items() + value_serializer.errors.items()),
                        status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.info("error = %s" % e)
            return Response("Error in adding post", status=status.HTTP_400_BAD_REQUEST)
        return Response("Post added successfully", status=status.HTTP_201_CREATED)
