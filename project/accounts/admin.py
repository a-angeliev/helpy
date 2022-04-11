from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model

from project.accounts.models import Profile
from project.main.models import Shelter, Job, Campaign

UserModel = get_user_model()


class SomeInline(admin.TabularInline):
    model = Profile


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    inlines = [SomeInline]
    # inlines = (PetInlineAdmin,)
    # list_display = ('first_name', 'last_name')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Campaign)
class ProfileAdmin(admin.ModelAdmin):
    pass


# class AllUserAdmin(admin.ModelAdmin):
#     inlines = [UserAdmin, ProfileAdmin]


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


# @admin.register()
# class ShelterAdmin(admin.ModelAdmin):
#     # inlines = (PetInlineAdmin,)
#     list_display = ('first_name', 'last_name')
