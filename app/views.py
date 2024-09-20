from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class UsersIndex(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = UserSerializer




