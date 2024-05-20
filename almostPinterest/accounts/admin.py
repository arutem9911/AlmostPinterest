from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')  # Определите, какие поля отображать в списке пользователей
    list_filter = ('is_staff', 'is_active')  # Фильтры для списка пользователей
    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # Определите, какие поля отображать в форме редактирования пользователя
        ('Permissions', {'fields': ('is_staff', 'is_active')}),  # Дополнительные разрешения пользователя
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email',)  # Поля, по которым будет производиться поиск пользователей
    ordering = ('email',)  # Порядок сортировки пользователей


# Регистрация модели и административного класса
admin.site.register(CustomUser, CustomUserAdmin)
