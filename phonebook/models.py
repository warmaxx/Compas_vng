from django.db import models
from homepage.models import Region, FedRegion, Job, Rank, STATUS_CONTACT_CHOICES


DEPARTAMENT_TYPE = [
    (1, 'Округ'),
    (2, 'Отдел'),
    (3, 'Отделение'),
    (4, 'Группа'),
]


class Departament(models.Model):
    name = models.CharField('Полное название отдела', max_length=100)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, blank=True, verbose_name='Регион')
    address = models.CharField('Адрес местонахождения отдела', max_length=100, blank=True)
    type = models.IntegerField('Тип подразделения', choices=DEPARTAMENT_TYPE)
    position = models.IntegerField('Порядковый номер', help_text='Чем меньше номер, тем выше в списке.')
    count_employees = models.IntegerField('Количество по штату')

    def __str__(self):
        return str(self.name) + " | " + str(self.region)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Contact(models.Model):
    sur_name = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100, blank=True)
    departament = models.ForeignKey(Departament, on_delete=models.PROTECT, verbose_name='Отдел')
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность')
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT, verbose_name='Звание')
    work_phone = models.CharField('Служебный номер', max_length=100, blank=True)
    cell_phone = models.CharField('Мобильный номер', max_length=100, blank=True)
    email = models.EmailField('E-mail @rosgvard.ru', max_length=100, blank=True)
    comment = models.TextField('Комментарий', blank=True)
    status = models.IntegerField('Статус', choices=STATUS_CONTACT_CHOICES)

    def __str__(self):
        return str(self.rank.full_name) + " | " + str(self.sur_name) + " " + str(self.name) + " " + str(
            self.patronymic) + " | " + str(self.departament.name) + " | " + str(self.departament.region.name)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

