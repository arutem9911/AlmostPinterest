from django.contrib import admin
from comments.models import Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('photo', 'email_author', 'created_at', 'text')

    search_fields = ('text', 'email__author')  # Поля для поиска
    readonly_fields = ('created_at',)

    def email_author(self, obj):
        return obj.author.email  # Определяем метод для отображения имени автора в списке объектов

    email_author.short_description = 'Author'  # Определяем пользовательское имя для поля в списке объектов


admin.site.register(Comment, CommentAdmin)
