from django.contrib import admin
from .models import *


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'available']
    search_fields = ['name']
    list_editable = ['available']
    list_filter = ['name']


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name', 'description', 'available', 'phone']
    search_fields = ['last_name']
    list_editable = ['available']
    list_filter = ['last_name']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'available']
    list_editable = ['available']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'available', 'district']
    search_fields = ['name']
    list_editable = ['available']
    list_filter = ['district']