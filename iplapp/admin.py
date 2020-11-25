from django.contrib import admin
from iplapp.models import Team

# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'home_city',]