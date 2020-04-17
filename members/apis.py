from django.contrib.auth import get_user_model
from rest_framework import generics

from members.serializers import UserSerializer

User = get_user_model()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer()


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.object.all()
    serializer_class = UserSerializer()
