from django.db import models
from homepage.models import Region, FedRegion, Job, Rank, Departament


class Status(models.Model):
    name = models.CharField('Статус сотрудника', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Contact(models.Model):
    sur_name = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100, blank=True)
    departament = models.ForeignKey(Departament, on_delete=models.PROTECT, blank=True)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, blank=True)
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT, blank=True)
    work_phone = models.CharField('Служебный номер', max_length=100, blank=True)
    cell_phone = models.CharField('Мобильный номер', max_length=100, blank=True)
    email = models.CharField('E-mail @rosgvard.ru', max_length=100, blank=True)
    comment = models.TextField('Комментарий', blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return str(self.rank.full_name) + " | " + str(self.sur_name) + " " + str(self.name) + " " + str(self.patronymic) + " | " + str(self.departament.name) + " | " + str(self.departament.region.name)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
