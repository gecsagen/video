from django.contrib import admin
from .models import PhotoVideoFile


@admin.register(PhotoVideoFile)
class PhotoVideoFileAdmin(admin.ModelAdmin):
    """Регистрация модели PhotoVideoFile в админке."""
    list_display = ("file_type", "file", "size", "created_at", "recognition_result")
    list_filter = ("file_type", "created_at")
    search_fields = ("file", "recognition_result")
