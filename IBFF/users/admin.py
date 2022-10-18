from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import IBFFUser


class IBFFUserAdmin(UserAdmin):
    model = IBFFUser
    list_display = ["username"]


admin.site.register(IBFFUser, IBFFUserAdmin)
