from UserPost.models import *
from rest_framework import serializers


class UserPostSerializer(serializers.ModelSerializer):
	"""
	Serializer for user post.
	"""
	class Meta:
		model = UserPost

class GetUserPostSerializer(serializers.ModelSerializer):
    """
    Serializer for getting user post.
    """
    class Meta:
        model = UserPost
        fields = ('user_post', 'connected_user', 'first_name', 'middle_name', 'last_name', 'image', 'created_at', 'modified_at')
