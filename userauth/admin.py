from django.contrib import admin
from userauth import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Profile)
