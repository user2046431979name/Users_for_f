from django.contrib import admin
from .models import *

class UAdmin(admin.ModelAdmin):
     list_display = ("id","name","email",)
     search_fields = ("name","dateBirth")
     list_filter = ("dateBirth","name","id")



admin.site.register(People,UAdmin)

