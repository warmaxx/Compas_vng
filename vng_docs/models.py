from django.db import models

# Create your models here.


class Folder(models.Model):
    name = models.CharField('Название раздела', unique=True, max_length=200)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField('Название шаблона', unique=True, max_length=200)
    doc = models.FileField('Файл', upload_to='vng_docs/docs/')
    image = models.ImageField('Изображение файла', upload_to='vng_docs/image/')
    folder = models.ForeignKey(Folder, verbose_name='Раздел', related_name='files', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Шаблон документа'
        verbose_name_plural = 'Шаблоны документов'

    def __str__(self):
        return self.name
