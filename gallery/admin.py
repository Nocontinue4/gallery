from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'created_at')
    search_fields = ('image_name',)
