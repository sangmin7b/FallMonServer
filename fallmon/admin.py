from django.contrib import admin

# Register your models here.

from .models import User, FallType, FallHistory

admin.site.register(User)
admin.site.register(FallType)
admin.site.register(FallHistory)
