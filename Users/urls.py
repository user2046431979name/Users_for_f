from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',UsersIndex.as_view()),
    path('userDetail/<int:pk>',UserDetail.as_view())
]
