from django.contrib import admin
from .models import *

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'available', 'is_paid', 'get_coaches', 'get_places', 'get_districts']
    search_fields = ['name']
    list_editable = ['available', 'is_paid']
    list_filter = ['name']
    
    def get_coaches(self, obj):
        return ", ".join([str(coach) for coach in obj.coach.all()])
    get_coaches.short_description = 'Тренеры'
    
    def get_places(self, obj):
        return ", ".join([str(place) for place in obj.place.all()])
    get_places.short_description = 'Места'
    
    def get_districts(self, obj):
        return ", ".join([str(district) for district in obj.district.all()])
    get_districts.short_description = 'Районы'


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name', 'description', 'available', 'phone']
    search_fields = ['first_name', 'last_name', 'middle_name']
    list_editable = ['available']
    list_filter = ['available', 'phone']

