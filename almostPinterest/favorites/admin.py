from django.contrib import admin
from favorites.models import Favorite


# Register your models here.
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo')

    search_fields = ('user', 'photo')  # Поля для поиска

    def user(self, obj):
        return obj.user.email  # Определяем метод для отображения имени автора в списке объектов

    user.short_description = 'User'  # Определяем пользовательское имя для поля в списке объектов


admin.site.register(Favorite, FavoriteAdmin)
