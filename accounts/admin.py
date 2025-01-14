from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'subscription',
        'subscription_start',
        'subscription_end',
        'is_active',
    )

    list_filter = (
        'role',
        'subscription',
        'is_active',
        'is_staff',
        'is_superuser',
    )

    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )

    ordering = ('-date_joined',)

    fieldsets = (
        ('اطلاعات حساب', {
            'fields': (
                'username',
                'password',
            )
        }),

        ('اطلاعات شخصی', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'avatar',
            )
        }),

        ('اشتراک', {
            'fields': (
                'subscription',
                'subscription_start',
                'subscription_end',
            )
        }),

        ('نقش کاربر', {
            'fields': (
                'role',
            )
        }),

        ('دسترسی‌ها', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),

        ('تاریخ‌ها', {
            'fields': (
                'last_login',
                'date_joined',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'role',
                'subscription',
            ),
        }),
    )