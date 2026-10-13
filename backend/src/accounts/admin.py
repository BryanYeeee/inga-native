from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Field workers do not self-register, so accounts are created here for now.
admin.site.register(User, UserAdmin)
