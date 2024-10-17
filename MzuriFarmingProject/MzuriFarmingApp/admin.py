from django.contrib import admin
from .models import Crops

@admin.register(Crops)
class CropsAdmin(admin.ModelAdmin):
    list_display = ['id', 'crop_name', 'scientific_name', 'average_yield', 'classification']
