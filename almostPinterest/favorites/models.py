from django.db import models
from django.conf import settings
from app.models import Photo


# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'photo',)
