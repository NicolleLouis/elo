from django.contrib import admin
import django.contrib.auth.models
from django.contrib import auth

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
