from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


# Create your models here.
class Following(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followings')
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')

    # На одного человека нельзя несколько раз подписываться
    class Meta:
        unique_together = ('follower', 'following',)

    # На самого себя нельзя подписываться
    def clean(self):
        if self.follower == self.following:
            raise ValidationError("The user cannot follow himself.")
