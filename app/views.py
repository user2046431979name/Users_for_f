from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class UsersViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = UserSerializer



