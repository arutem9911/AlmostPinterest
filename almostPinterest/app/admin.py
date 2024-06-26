from django.contrib import admin
from app.models import Photo


# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', 'email_author', 'created_at', 'description', 'title')

    search_fields = ('title', 'email__author')  # Поля для поиска
    readonly_fields = ('created_at', )

    def email_author(self, obj):
        return obj.author.email  # Определяем метод для отображения имени автора в списке объектов

    email_author.short_description = 'Author'  # Определяем пользовательское имя для поля в списке объектов


admin.site.register(Photo, PhotoAdmin)
