from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

# Register your models here.
class UserAdmin(UserAdmin):
    model = User
    
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)