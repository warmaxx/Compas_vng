from django.db import models
from homepage.models import Region


class TekInfo(models.Model):
    region = models.OneToOneField(Region, on_delete=models.CASCADE, unique=True, verbose_name='Регион')
    # Проверки ТЭК
    tek_plan_check = models.IntegerField('ТЭК Количество плановых проверок', default=0)
    tek_out_plan_check = models.IntegerField('ТЭК Количество внеплановых проверок', default=0)
    tek_ls = models.IntegerField('ТЭК Количество задействованого л\с', default=0)
    # Направление ТЭК
    tek_high = models.IntegerField('Количество высоких', default=0)
    tek_mid = models.IntegerField('Количество средних', default=0)
    tek_low = models.IntegerField('Количество низких', default=0)
    # Проверки подразделения охраны
    vo_plan_check = models.IntegerField('ТЭК Количество плановых проверок', default=0)
    vo_out_plan_check = models.IntegerField('ТЭК Количество внеплановых проверок', default=0)
    vo_ls = models.IntegerField('ТЭК Количество задействованого л\с', default=0)
    # Направление подразделение охраны (VO)
    vo_deps_foiv = models.IntegerField('Подразделения охраны - ФОИВ', default=0)
    vo_deps_ul = models.IntegerField('Подразделения охраны - организаций', default=0)
    vo_deps_ul_special = models.IntegerField('Подразделения охраны - ЮЛ с особыми уставными задачами', default=0)
    # Численность
    vo_pers_vo = models.IntegerField('Численность ВО', default=0)
    vo_pers_special = models.IntegerField('Численность ЮЛ с особыми уставными задачами', default=0)
    # Количество объектов
    vo_obj_vo = models.IntegerField('Объектов ВО', default=0)
    vo_obj_special = models.IntegerField('Объектов ЮЛ с особыми уставными задачами', default=0)
    # Количество оружия
    vo_guns_army = models.IntegerField('Оружия боевого', default=0)
    vo_guns_work = models.IntegerField('Оружия служебного', default=0)
    vo_guns_civil = models.IntegerField('Оружия гражданского', default=0)
    vo_guns_study = models.IntegerField('Оружия учебного', default=0)

    def __str__(self):
        return str(self.region)

    class Meta:
        verbose_name = 'Информация о регионе'
        verbose_name_plural = 'Информация о регионе'