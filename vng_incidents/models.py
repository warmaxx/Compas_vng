from django.db import models
from django.utils import timezone

from homepage.models import Region


SOURCE_CHOICE = [
    ('СМИ', 'СМИ'),
    ('Доклад тер. подр.', 'Доклад тер. подр.')
]

SUBJECT_CHOICE = [
    ('Объект ТЭК', 'Объект ТЭК'),
    ('Ведомственная охрана', 'Ведомственная охрана')
]


class Incident(models.Model):
    date_time = models.DateTimeField('Дата и время происшествия')
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Регион')
    source = models.CharField('Источник', choices=SOURCE_CHOICE, max_length=20)
    subject = models.CharField('Субъект происшествия', choices=SUBJECT_CHOICE, max_length=22)
    inc_text = models.TextField('Происшествие')
    result = models.TextField('Результат', blank=True)
    comment = models.TextField('Примечание', blank=True)

    def __str__(self):
        return str(self.date_time) + " | " + str(self.inc_text[:50])

    class Meta:
        verbose_name = 'Происшествие'
        verbose_name_plural = 'Происшествия'
