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
    select_region_name = ''
    count_deps_gk = ''
    count_deps_type_2 = ''
    count_deps_type_3 = ''
    count_deps_type_4 = ''
    count_pers_plan = ''
    count_pers_fact = ''
    count_pers_result = ''
    count_pers_result_percent = ''
    if request.method == 'POST':
        select_region_id = request.POST.get('region_id')
        select_region_name = Region.objects.filter(id=select_region_id).values_list('name', flat=True)
        select_region_name = select_region_name[0]
        try:
            info = TekInfo.objects.get(region=select_region_id)
            count_deps_gk = Departament.objects.filter(region=select_region_id).filter(type__in=(2, 3, 4)).count()
            count_deps_type_2 = Departament.objects.filter(region=select_region_id).filter(type=2).count()
            count_deps_type_3 = Departament.objects.filter(region=select_region_id).filter(type=3).count()
            count_deps_type_4 = Departament.objects.filter(region=select_region_id).filter(type=4).count()
            count_pers_plan = Departament.objects.values('region').filter(region=select_region_id).filter(
                type__in=(2, 3, 4)).annotate(
                Sum('count_employees'))
            count_pers_plan = count_pers_plan[0]['count_employees__sum']
            count_pers_fact = Contact.objects.filter(departament__region=select_region_id).filter(
                departament__type__in=(2, 3, 4)).count()
            count_pers_result = count_pers_plan - count_pers_fact
            count_pers_result_percent = round(
                ((count_pers_plan - count_pers_fact) / count_pers_plan) * 100, 2)
        except Exception as e:
            info = ''

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
        'select_region_id': int(select_region_id),
        'select_region_name':select_region_name,
        'count_deps_gk': count_deps_gk,
        'count_deps_type_2': count_deps_type_2,
        'count_deps_type_3': count_deps_type_3,
        'count_deps_type_4': count_deps_type_4,
        'count_pers_plan': count_pers_plan,
        'count_pers_fact': count_pers_fact,
        'count_pers_result': count_pers_result,
        'count_pers_result_percent': count_pers_result_percent,
    }
    return render(request, 'homepage/index.html', context)
