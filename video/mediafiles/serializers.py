from rest_framework import serializers
from .models import PhotoVideoFile


class PhotoVideoFileSerializer(serializers.ModelSerializer):
    """Основной сериализатор для PhotoVideoFile."""
    class Meta:
        model = PhotoVideoFile
        fields = ('file_type', 'file')


class PhotoVideoListSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения списка объектов."""
    class Meta:
        model = PhotoVideoFile
        fields = fields = '__all__'


class PhotoVideoDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения 1 объекта."""
    class Meta:
        model = PhotoVideoFile
        fields = fields = '__all__'