from django.contrib import admin
from tickets.models import Tickets


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'client', 'support_ticket', 'created_at')  # Добавление столбцов в админке.
    list_display_links = ('id', 'title')  # Чтобы в админке название стало ссылкой(а не только id)
    # search_fields = ('title', 'content')  # Поиск по полям в админке( указать по каким полям)
    # list_filter = ('is_published', 'category')  # фильтровать
    save_on_top = True  # Добавляет панель с кнопками (сохранить..) сверху в админке


admin.site.register(Tickets, TicketsAdmin)
admin.site.site_header = 'Управление заявками'
