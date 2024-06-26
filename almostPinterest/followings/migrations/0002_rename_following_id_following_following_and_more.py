# Generated by Django 5.0.6 on 2024-05-20 18:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='following',
            old_name='following_id',
            new_name='following',
        ),
        migrations.AlterUniqueTogether(
            name='following',
            unique_together={('follower', 'following')},
        ),
    ]
