from django.contrib import admin

# Register your models here.
from project.main.models import Questionnaire, Campaign, Shelter, Job


@admin.register(Questionnaire)
class Questionnaire(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title",)