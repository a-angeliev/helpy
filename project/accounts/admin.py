from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model

from project.accounts.models import Profile

UserModel = get_user_model()


class SomeInline(admin.TabularInline):
    model = Profile


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    inlines = [SomeInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass





