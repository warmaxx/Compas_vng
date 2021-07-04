from django.db import models


class Modul_1_1(models.Model):
    date = models.DateField('Дата')
    name_from = models.CharField('Наименование объекта куда направлена информация', max_length=200)
    text = models.TextField('Описательная часть')
    output_number_date = models.CharField('Исходящий номер документа и число (дата)', max_length=200)
    person = models.CharField('Исполнитель', max_length=100)

    def __str__(self):
        return str(self.date) + " | " + str(self.name_from)

    class Meta:
        verbose_name = 'Модуль 1_1 (Подготовлены и направлены)'
        verbose_name_plural = 'Модули 1_1 (Подготовлены и направлены)'
