from atexit import register
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', ]
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'bio', 'phone', 'photo')}),
    )
