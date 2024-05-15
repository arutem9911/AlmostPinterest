from django.db import models
from django.conf import settings


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')  # Поле для загрузки изображения
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')  # Внешний ключ к пользователю
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания фотографии
    description = models.TextField(blank=True)  # Описание фотографии, не обязательное поле
    title = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return f'Photo by {self.author.email} uploaded at {self.created_at}'
