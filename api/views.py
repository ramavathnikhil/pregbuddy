from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics

from api.serializers import UserSerializer, GroupSerializer, AuthorSerializer, BucketlistSerializer
from .models import Author


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AuthorView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Author
    serializer_class = AuthorSerializer


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Author.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
