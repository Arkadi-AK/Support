from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

from support.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class Tickets(models.Model):
    class TicketStatus(models.TextChoices):
        wait = 0, gettext_lazy('Solved')
        works = 1, gettext_lazy('Unresolved')
        done = 2, gettext_lazy('Frozen')

    status = models.CharField(
        max_length=2,
        choices=TicketStatus.choices,
        default=TicketStatus.wait,
        verbose_name='Статус заявки',
    )

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
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'


class Messages(models.Model):
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', default=None, null=True, blank=True,
                               on_delete=models.CASCADE, verbose_name='parent',
                               related_name='replys')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Massage by {self.user.name} on {self.ticket}'

    def children(self):
        return Messages.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
