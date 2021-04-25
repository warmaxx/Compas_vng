from django.db import models

# Create your models here.
class Ul (models.Model):
    name = models.CharField('Название юридического лица',max_length=100)
    place = models.CharField('Местонахождение юридического лица',max_length=100)
    INN = models.IntegerField('ИНН юридического лица')
    OGRN = models.IntegerField('ОГРН юридического лица')

class Category (models.Model):
    name = models.CharField('Название категории объекта', max_length=100)

class Form (models.Model):
    name = models.CharField('Название формы проверки', max_length=100)

class Tek_Object (models.Model):
    name = models.CharField('Название объекта', max_length=100)
    place = models.CharField('Местонахождение объекта', max_length=100)
    ul = models.ForeignKey(Ul, on_delete=models.CASCADE)
    category = models.ForeignKey(Category)


class Check (models. Model):
    tek_Object = models.ForeignKey(Tek_Object, on_delete=models.CASCADE)
    date_latest_check = models.DateField('Дата окончания последней проверки')
    date_next_check = models.DateField('Дата начала проведения следующей проверки')
    duration = models.IntegerField('Срок проведения проверки (Рабочих дней)')
    form = models.ForeignKey(Form)