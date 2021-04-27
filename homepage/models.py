from django.db import models

# Create your models here.

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


