from django.contrib import admin

# Register your models here.
from django.contrib import admin

from project.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name')