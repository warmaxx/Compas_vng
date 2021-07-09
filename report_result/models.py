from django.db import models


class Recipient(models.Model):
    name = models.CharField('Получатель',
                            max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


class Modul_1_1(models.Model):
    date = models.DateField('Дата')
    name_from = models.ForeignKey(Recipient,
                                  verbose_name='Наименование объекта куда направлена информация',
                                  on_delete=models.CASCADE)
    text = models.TextField('Описательная часть')
    input_number = models.CharField('Входящий номер документа',
                                    max_length=200,
                                    blank=True,
                                    null=True)
    input_date = models.DateField('Дата входящего документа',
                                  max_length=200,
                                  blank=True,
                                  null=True)
    output_number = models.CharField('Исходящий номер документа',
                                     max_length=200,
                                     blank=True,
                                     null=True)
    output_date = models.DateField('Дата исходящего документа',
                                   max_length=200,
                                   blank=True,
                                   null=True)
    person = models.CharField('Исполнитель',
                              max_length=100)

    def __str__(self):
        return str(self.date) + " | " + str(self.name_from) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 1_1 (Подготовлены и направлены)'
        verbose_name_plural = 'Материалы модуля 1_1 (Подготовлены и направлены)'


class Modul_1_2(models.Model):
    date = models.DateField('Дата')
    name_from = models.ForeignKey(Recipient,
                                  verbose_name='Наименование объекта куда направлена информация',
                                  on_delete=models.CASCADE)
    text = models.TextField('Описательная часть')

    input_number = models.CharField('Входящий номер документа',
                                    max_length=200,
                                    blank=True,
                                    null=True)
    input_date = models.DateField('Дата входящего документа',
                                  max_length=200,
                                  blank=True,
                                  null=True)
    output_number = models.CharField('Исходящий номер документа',
                                     max_length=200,
                                     blank=True,
                                     null=True)
    output_date = models.DateField('Дата исходящего документа',
                                   max_length=200,
                                   blank=True,
                                   null=True)

    person = models.CharField('Исполнитель',
                              max_length=100)

    def __str__(self):
        return str(self.date) + " | " + str(self.name_from) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 1_2 (Подготовлены и представлены)'
        verbose_name_plural = 'Материалы модуля 1_2 (Подготовлены и представлены)'


class Modul_3(models.Model):
    date = models.DateField('Дата')
    text = models.TextField('Описательная часть')

    def __str__(self):
        return str(self.date) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 3 (О состоянии нормативной правовой работы в установленных сферах служебной деятельности)'
        verbose_name_plural = 'Материалы модуля 3 (О состоянии нормативной правовой работы в установленных сферах служебной деятельности)'


class Modul_4_1(models.Model):
    date = models.DateField('Дата')
    text = models.TextField('Описательная часть')
    executor_foiv = models.TextField('Исполнитель от ФОИВ',
                                     blank=True,
                                     null=True)
    executor_vng = models.TextField('Исполнитель от Росгвардии',
                                    blank=True,
                                    null=True)
    executor_gu = models.TextField('Исполнитель от ГУЛРРиГК',
                                   blank=True,
                                   null=True)
    date_end = models.TextField('Срок')
    result = models.TextField('Проделанная работа')

    def __str__(self):
        return str(self.date) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 4_1 (Находящиеся на исполнении поручения)'
        verbose_name_plural = 'Материалы модуля 4_1 (Находящиеся на исполнении поручения)'


class Modul_4_2(models.Model):
    date = models.DateField('Дата')
    text = models.TextField('Описательная часть')
    executor_foiv = models.TextField('Исполнитель от ФОИВ',
                                     blank=True,
                                     null=True)
    executor_vng = models.TextField('Исполнитель от Росгвардии',
                                    blank=True,
                                    null=True)
    executor_gu = models.TextField('Исполнитель от ГУЛРРиГК',
                                   blank=True,
                                   null=True)
    date_end = models.TextField('Срок')
    result = models.TextField('Проделанная работа')

    def __str__(self):
        return str(self.date) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 4_2 (Исполненные поручения)'
        verbose_name_plural = 'Материалы модуля 4_2 (Исполненные поручения)'


class Modul_5(models.Model):
    date = models.DateField('Дата')
    text = models.TextField('Описательная часть')

    def __str__(self):
        return str(self.date) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 5'
        verbose_name_plural = 'Материалы модуля 5'


class Modul_6(models.Model):
    date = models.DateField('Дата')
    text = models.TextField('Описательная часть')
    result = models.TextField('Проделанная работа')

    def __str__(self):
        return str(self.date) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 6'
        verbose_name_plural = 'Материалы модуля 6'


class Modul_7(models.Model):
    date = models.DateField('Дата')
    text = models.TextField('Описательная часть')

    def __str__(self):
        return str(self.date) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 7'
        verbose_name_plural = 'Материалы модуля 7'


class Modul_8(models.Model):
    date = models.DateField('Дата')
    text = models.TextField('Описательная часть')

    def __str__(self):
        return str(self.date) + " | " + str(self.text)[:50]

    class Meta:
        verbose_name = 'Материал модуля 8'
        verbose_name_plural = 'Материалы модуля 8'
