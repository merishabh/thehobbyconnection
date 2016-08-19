from hobbyapp.models import *
from rest_framework import serializers


class UserSaveSerializer(serializers.ModelSerializer):
	"""
	Serializer for user post.
	"""
	class Meta:
		model = User
