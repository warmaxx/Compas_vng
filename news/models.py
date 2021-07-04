from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст', null=False, blank=False)
    date_create = models.DateField('Дата создания / редактирования новости',
                                   auto_now=True,
                                   editable=False,
                                   blank=True)
    date_start = models.DateField('Дата с которой нужно показывать новость')
    date_end = models.DateField('Дата до которой нужно показывать новость')
    image = models.ImageField('Изображение', upload_to='news/image/%Y/%m/%d/', blank=True)
    doc = models.FileField('Файл с документом', upload_to='news/result_report/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
