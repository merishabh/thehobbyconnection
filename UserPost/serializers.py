from UserPost.models import *
from rest_framework import serializers


class UserPostSerializer(serializers.ModelSerializer):
	"""
	Serializer for user post.
	"""
	# posted_by = serializers.RelatedField(source='connected_user', read_only=True)
	class Meta:
		model = UserPost
		
