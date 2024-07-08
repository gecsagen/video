from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import upload_video, record_video_page, PhotoVideoFileViewSet

router = DefaultRouter()
router.register(r"files", PhotoVideoFileViewSet, basename="files")

urlpatterns = [
    path("upload_video/", upload_video, name="upload_video"),
    path("record_video/", record_video_page, name="record_video_page"),
    path("", include(router.urls)),
]
