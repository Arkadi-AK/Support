from django.contrib import admin

# Register your models here.
from tickets.models import Tickets


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'client', 'support_ticket', 'created_at')  # Добавление столбцов в админке.
    list_display_links = ('id', 'title')  # Чтобы в админке название новости стало ссылкой(а не только id)
    # search_fields = ('title', 'content')  # Поиск по полям в админке( указать по каким полям)
    # list_editable = ('is_published',)  # Можно сделать, чтобы редактировалось поле опубликовано из админки
    # list_filter = ('is_published', 'category')  # фильтровать
    # fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at',
    #           'updated_at')  # Чтобы выводилась фото в админке, при создании новости.
    # readonly_fields = ('get_photo', 'views', 'created_at',
    #                    'updated_at')  # Тут указываются поля, которые нужны только для чтения. Их пользователь не может менять
    save_on_top = True  # Добавляет панель с кнопками (сохранить..) сверху в админке


admin.site.register(Tickets, TicketsAdmin)


admin.site.site_header = 'Управление заявками'