from rest_framework import generics
from .serializers import UserSerializer
from .permissions import IsMeOrReadOnly
from rest_framework import permissions
from django.contrib.auth.models import User


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsMeOrReadOnly | permissions.IsAdminUser]

