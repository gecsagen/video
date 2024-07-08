from django.db import models


class PhotoVideoFile(models.Model):
    """Модель для фото/видео."""
    FILE_TYPES = (
        ("photo", "Photo"),
        ("video", "Video"),
    )

    file_type = models.CharField(verbose_name="Тип файла", max_length=5, choices=FILE_TYPES)
    file = models.FileField(verbose_name="Файл", upload_to="uploads/")
    size = models.PositiveIntegerField(verbose_name="Размер файла", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    recognition_result = models.JSONField(verbose_name="Результат распознавания", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.file and not self.size:
            self.size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.file.name} ({self.file_type})"
