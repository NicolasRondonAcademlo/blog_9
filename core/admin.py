from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import  UserAdmin as BaseUserAdmin
User = get_user_model()
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    list_display = ["email", "admin"]
    list_filter = ["admin"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info",{"fields": ("cellphone", "name")}),
        ("Permissions", {"fields":("admin",)}),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()

admin.site.register(User, UserAdmin)