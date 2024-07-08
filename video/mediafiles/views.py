# mediafiles/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PhotoVideoFile
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import PhotoVideoFile
from .serializers import (
    PhotoVideoFileSerializer,
    PhotoVideoListSerializer,
    PhotoVideoDetailSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from .utils import detect_objects


class PhotoVideoFileViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели PhotoVideoFile."""
    queryset = PhotoVideoFile.objects.all()
    serializer_class = PhotoVideoFileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_class(self):
        if self.action == "create":
            return PhotoVideoFileSerializer
        elif self.action == "list":
            return PhotoVideoListSerializer
        elif self.action == "retrieve":
            return PhotoVideoDetailSerializer
        return PhotoVideoFileSerializer

    def create(self, request, *args, **kwargs):
        file = request.data.get("file")
        if file:
            # Сохраняем файл в модель
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            instance = serializer.instance

            # Выполняем распознавание объектов
            recognition_result = detect_objects(instance.file.path)

            # Сохраняем результат распознавания в модели
            instance.recognition_result = recognition_result
            instance.save()

            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(
                {"status": "error", "message": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST,
            )


@csrf_exempt
def upload_video(request):
    """Представлене для загрузки видео из браузера."""
    if request.method == "POST":
        file = request.FILES.get("video")
        if file:
            video = PhotoVideoFile.objects.create(
                file_type="video", file=file, size=file.size
            )
            return JsonResponse({"status": "success", "id": video.id})
        return JsonResponse(
            {"status": "error", "message": "No file uploaded"}, status=400
        )
    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=405
    )


def record_video_page(request):
    """Представление для рендера формы записи видео."""
    return render(request, "record_video.html")
