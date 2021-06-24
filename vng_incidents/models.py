from django.db import models
from homepage.models import Region

SOURCE_CHOICE = [
    (1, 'СМИ'),
    (2, 'Доклад тер. подр.')
]


class Incident(models.Model):
    date_time = models.DateTimeField('Дата и время происшествия', auto_now=True, editable=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Регион')
    source = models.IntegerField('Источник', choices=SOURCE_CHOICE)
    subject = models.TextField('Субьект происшествия')
    inc_text = models.TextField('Происшествие')
    result = models.TextField('Результат')
    comment = models.TextField('Примечание')

    def __str__(self):
        return str(self.date_time) + " | " + str(self.inc_text[:50])

    class Meta:
        verbose_name = 'Происшествие'
        verbose_name_plural = 'Происшествия'
