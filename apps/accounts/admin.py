from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.accounts.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "get_groups_display")

    def get_groups_display(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    get_groups_display.short_description = "Groups"


admin.site.register(User, UserAdmin)
