from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Topic


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
#
#
# class AuthorSerializer(serializers.ModelSerializer):
#     """
#     Serializing all the Authors
#     """
#
#     class Meta:
#         model = Author
#         fields = ('id', 'first_name', 'last_name')
#
#
# class BucketlistSerializer(serializers.ModelSerializer):
#     """Serializer to map the Model instance into JSON format."""
#
#     class Meta:
#         """Meta class to map serializer's fields with the model fields."""
#         model = Author
#         fields = ('id', 'name', 'date_created', 'date_modified')
#         read_only_fields = ('date_created', 'date_modified')


class TopicSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Topic
        fields = ('id', 'topic_text', 'user_id', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
