from django.contrib import admin
from followings.models import Following


# Register your models here.
class FollowingAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following')

    search_fields = ('follower', 'following')  # Поля для поиска

    def follower(self, obj):
        return obj.follower.email

    def following_id(self, obj):
        return obj.following_id.email  # Определяем метод для отображения имени автора в списке объектов

    follower.short_description = 'Follower'  # Определяем пользовательское имя для поля в списке объектов
    following_id.short_description = 'Following'  # Определяем пользовательское имя для поля в списке объектов


admin.site.register(Following, FollowingAdmin)
