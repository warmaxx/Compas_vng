from django.shortcuts import render
from django.db.models import Q
from vng_stat.models import Tek_Object, Ul
from news.models import News
from vng_incidents.models import Incident
from homepage.models import Region, FedRegion
from vng_info.models import TekInfo
from phonebook.models import Departament, Contact
import datetime as dt
from django.db.models import Sum


def index(request):
    now = dt.datetime.now()
    count_ul = Ul.objects.count()
    count_all = Tek_Object.objects.count()
    count_high = Tek_Object.objects.filter(category__name='Высокая').count()
    count_medium = Tek_Object.objects.filter(category__name='Средняя').count()
    count_low = Tek_Object.objects.filter(category__name='Низкая').count()
    news = News.objects.filter(date_start__lte=now).filter(date_end__gte=now).order_by('id').reverse()
    regions = Region.objects.all().order_by('name')
    fed_regions = FedRegion.objects.all().order_by('name')

    incidents = Incident.objects.all()
    now = dt.datetime.now()
    day_now = now.day
    month_now = now.month
    year_now = now.year
    count_now_year = incidents.filter(date_time__year=year_now).count()
    count_last_day = incidents.filter(Q(date_time__year=year_now),
                                      Q(date_time__month=month_now),
                                      Q(date_time__day=day_now),

                                      ).count()
    info = ''
    select_region_id = '0'
    select_fed_region_id = '0'
    select_region_name = ''
    select_fed_region_name = ''
    count_deps_gk = ''
    count_deps_type_2 = ''
    count_deps_type_3 = ''
    count_deps_type_4 = ''
    count_pers_plan = ''
    count_pers_fact = ''
    count_pers_result = ''
    count_pers_result_percent = ''

    select_stat = 0
    count_pers_work = Contact.objects.filter(status=0).filter(departament__type__in=(2, 3, 4)).count()
    count_pers_ill = Contact.objects.filter(status=1).filter(departament__type__in=(2, 3, 4)).count()
    count_pers_travel = Contact.objects.filter(status=2).filter(departament__type__in=(2, 3, 4)).count()
    count_pers_holiday = Contact.objects.filter(status=3).filter(departament__type__in=(2, 3, 4)).count()
    count_pers_pregnant = Contact.objects.filter(status=4).filter(departament__type__in=(2, 3, 4)).count()
    count_pers_study = Contact.objects.filter(status=5).filter(departament__type__in=(2, 3, 4)).count()
    count_pers_foreign = Contact.objects.filter(status=6).filter(departament__type__in=(2, 3, 4)).count()
    count_deps_gk = Departament.objects.filter(type__in=(2, 3, 4)).count()

    count_deps_type_2 = Departament.objects.filter(type=2).count()
    count_deps_type_3 = Departament.objects.filter(type=3).count()
    count_deps_type_4 = Departament.objects.filter(type=4).count()
    count_pers_plan = Departament.objects.filter(type__in=(2, 3, 4)).aggregate(
        count_employees__sum=Sum('count_employees'))
    count_pers_plan = count_pers_plan['count_employees__sum']
    if count_pers_plan is None:
        count_pers_plan = 0
    count_pers_fact = Contact.objects.filter(departament__type__in=(2, 3, 4)).count()
    count_pers_result = count_pers_plan - count_pers_fact
    try:
        count_pers_result_percent = round(
            ((count_pers_plan - count_pers_fact) / count_pers_plan) * 100, 2)
    except ZeroDivisionError:
        count_pers_result_percent = 0
    if request.method == 'POST':
        try:
            select_stat = request.POST.get('select_stat')
            if select_stat is None:
                select_stat = 0
            if int(select_stat) == 1:
                select_fed_region_name = 'Россия'
                info = TekInfo.objects.aggregate(
                    tek_high=Sum('tek_high'), tek_mid=Sum('tek_mid'), tek_low=Sum('tek_low'),
                    vo_deps_foiv=Sum('vo_deps_foiv'), vo_deps_ul=Sum('vo_deps_ul'),
                    vo_deps_ul_special=Sum('vo_deps_ul_special'),
                    vo_pers_vo=Sum('vo_pers_vo'), vo_pers_special=Sum('vo_pers_special'),
                    vo_obj_vo=Sum('vo_obj_vo'), vo_obj_special=Sum('vo_obj_special'),
                    vo_guns_army=Sum('vo_guns_army'), vo_guns_work=Sum('vo_guns_work'),
                    vo_guns_civil=Sum('vo_guns_civil'), vo_guns_study=Sum('vo_guns_study'),
                    tek_plan_check=Sum('tek_plan_check'), tek_out_plan_check=Sum('tek_out_plan_check'),
                    tek_ls=Sum('tek_ls'), vo_plan_check=Sum('vo_plan_check'),
                    vo_out_plan_check=Sum('vo_out_plan_check'),
                    vo_ls=Sum('vo_ls'),
                )
            if int(select_stat) == 2:
                try:
                    select_fed_region_id = request.POST.get('fed_region_id')
                    select_fed_region_name = FedRegion.objects.filter(id=select_fed_region_id).values_list('name',
                                                                                                           flat=True)
                    select_fed_region_name = select_fed_region_name[0]
                    info = TekInfo.objects.filter(region__fedname_id=select_fed_region_id).aggregate(
                        tek_high=Sum('tek_high'), tek_mid=Sum('tek_mid'), tek_low=Sum('tek_low'),
                        vo_deps_foiv=Sum('vo_deps_foiv'), vo_deps_ul=Sum('vo_deps_ul'),
                        vo_deps_ul_special=Sum('vo_deps_ul_special'),
                        vo_pers_vo=Sum('vo_pers_vo'), vo_pers_special=Sum('vo_pers_special'),
                        vo_obj_vo=Sum('vo_obj_vo'), vo_obj_special=Sum('vo_obj_special'),
                        vo_guns_army=Sum('vo_guns_army'), vo_guns_work=Sum('vo_guns_work'),
                        vo_guns_civil=Sum('vo_guns_civil'), vo_guns_study=Sum('vo_guns_study'),
                        tek_plan_check=Sum('tek_plan_check'), tek_out_plan_check=Sum('tek_out_plan_check'),
                        tek_ls=Sum('tek_ls'), vo_plan_check=Sum('vo_plan_check'),
                        vo_out_plan_check=Sum('vo_out_plan_check'),
                        vo_ls=Sum('vo_ls'),
                    )
                except Exception as e:
                    print(e)
                    info = ''
            if int(select_stat) == 3:
                select_region_id = request.POST.get('region_id')
                select_region_name = Region.objects.filter(id=select_region_id).values_list('name', flat=True)
                select_region_name = select_region_name[0]
                try:
                    info = TekInfo.objects.get(region=select_region_id)
                except Exception as e:
                    info = ''
                    print(e)
        except Exception as e:
            info = ''
            print(e)

    context = {
        'count_ul': count_ul,
        'count_all': count_all,
        'count_high': count_high,
        'count_medium': count_medium,
        'count_low': count_low,
        'news': news,
        'count_now_year': count_now_year,
        'count_last_day': count_last_day,
        'regions': regions,
        'fed_regions': fed_regions,
        'info': info,
        'select_stat': int(select_stat),
        'select_region_id': int(select_region_id),
        'select_fed_region_id': int(select_fed_region_id),
        'select_region_name': select_region_name,
        'select_fed_region_name': select_fed_region_name,
        'count_deps_gk': count_deps_gk,
        'count_deps_type_2': count_deps_type_2,
        'count_deps_type_3': count_deps_type_3,
        'count_deps_type_4': count_deps_type_4,
        'count_pers_plan': count_pers_plan,
        'count_pers_fact': count_pers_fact,
        'count_pers_result': count_pers_result,
        'count_pers_result_percent': count_pers_result_percent,
        'count_pers_work': count_pers_work,
        'count_pers_ill': count_pers_ill,
        'count_pers_travel': count_pers_travel,
        'count_pers_holiday': count_pers_holiday,
        'count_pers_pregnant': count_pers_pregnant,
        'count_pers_study': count_pers_study,
        'count_pers_foreign': count_pers_foreign,
    }
    return render(request, 'homepage/index.html', context)
