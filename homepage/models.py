from django.db import models


class FedRegion(models.Model):
    name = models.CharField('Название категории объекта', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Федеральный округ'
        verbose_name_plural = 'Федеральные округи'


class Region(models.Model):
    name = models.CharField('Название категории объекта', max_length=100)
    fedname = models.ForeignKey(FedRegion, on_delete=models.CASCADE)
    timezone = models.IntegerField('Часовой пояс региона GMT', default=0)

    def __str__(self):
        return str(self.name + " | " + str(self.timezone))

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Job(models.Model):
    full_name = models.CharField('Полное название должности', max_length=100)
    short_name = models.CharField('Сокращенное название должности', max_length=100)
    position = models.IntegerField('Порядковый номер')

    def __str__(self):
        return str(self.full_name) + " | " + str(self.position)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Rank(models.Model):
    full_name = models.CharField('Полное название звания', max_length=100)
    short_name = models.CharField('Сокращенное название звания', max_length=100)
    position = models.IntegerField('Порядковый номер')

    def __str__(self):
        return str(self.full_name) + " | " + str(self.position)

    class Meta:
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'


class Departament(models.Model):
    name = models.CharField('Полное название звания', max_length=100)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, blank=True)
    address = models.CharField('Адрес местонахождения отдела', max_length=100, blank=True)

    def __str__(self):
        return str(self.name) + " | " + str(self.region)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
