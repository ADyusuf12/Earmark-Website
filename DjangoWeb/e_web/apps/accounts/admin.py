from django.contrib import admin
from .models import UserPersona, UserProfile, UserInterest

admin.site.register(UserProfile)
admin.site.register(UserPersona)
admin.site.register(UserInterest)