from django.db import models
from django.conf import settings
from app.models import Photo


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Внешний ключ к пользователю
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания комментаря
