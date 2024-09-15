from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from app.views import *

router = DefaultRouter()
router.register(r"users",UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls