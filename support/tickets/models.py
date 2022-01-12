from django.db import models

from support.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class Tickets(models.Model):
    TICKET_STATUS = [
        (0, 'In waiting'),
        (1, 'In works'),
        (2, 'Done'),
    ]
    status = models.SmallIntegerField(choices=TICKET_STATUS, default=0, verbose_name='Статус заявки')
    client = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               limit_choices_to={'support': False},
                               related_name='client',
                               null=True,
                               verbose_name='Клиент')
    support_ticket = models.ForeignKey(User,
                                       on_delete=models.CASCADE,
                                       limit_choices_to={'support': True},
                                       related_name='supports', null=True,
                                       verbose_name='Специалист')
    title = models.CharField(max_length=255, null=False, verbose_name='Заголовок тикета')
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    star_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Тикет'  # Название  в единственном числе в админке
        verbose_name_plural = 'Тикеты'  # Название  во множественном числе в админке
