from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import UserProfile


class UserProfileAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email", "password1", "password2"),
            },
        ),
    )

admin.site.register(UserProfile, UserProfileAdmin)
