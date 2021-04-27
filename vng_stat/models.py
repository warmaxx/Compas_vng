from django.db import models
from homepage.models import Region

# Create your models here.
class Ul(models.Model):
    name = models.CharField('Название юридического лица', max_length=100)
    place = models.CharField('Местонахождение юридического лица', max_length=100)
    INN = models.IntegerField('ИНН юридического лица')
    OGRN = models.IntegerField('ОГРН юридического лица')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'


class Category(models.Model):
    name = models.CharField('Название категории объекта', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Form(models.Model):
    name = models.CharField('Название формы проверки', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма проверки'
        verbose_name_plural = 'Формы проверки'


class Tek_Object(models.Model):
    name = models.CharField('Название объекта', max_length=100)
    place = models.CharField('Местонахождение объекта', max_length=100)
    ul = models.ForeignKey(Ul, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект ТЭК'
        verbose_name_plural = 'Объекты ТЭК'


class Check(models.Model):
    tek_Object = models.ForeignKey(Tek_Object, on_delete=models.CASCADE)
    date_latest_check = models.DateField('Дата окончания последней проверки')
    date_next_check = models.DateField('Дата начала проведения следующей проверки')
    duration = models.IntegerField('Срок проведения проверки (Рабочих дней)')
    form = models.ForeignKey(Form, on_delete=models.PROTECT)
    target_text = models.TextField('Цель проведения проверки', default='Федеральный государственный контроль (надзор) за обеспечением безопасности объектов топливно-энергетического комплекса')
    target_link = models.TextField('Основание проведения проверки', default='п.22 ч. 1 ст. 9 Федерального закона от 3 июля 2016 г. № 226-ФЗ «О войсках национальной гвардии Российской Федерации»')

    def __str__(self):
        return str(self.id) + " | " + self.tek_Object.name + " | " + self.tek_Object.ul.name

    class Meta:
        verbose_name = 'Проверка'
        verbose_name_plural = 'Проверки'