from django.shortcuts import render
from django.db.models import Q
from vng_stat.models import Tek_Object, Ul
from news.models import News
from vng_incidents.models import Incident
import datetime as dt


def index(request):
    now = dt.datetime.now()
    count_ul = Ul.objects.count()
    count_all = Tek_Object.objects.count()
    count_high = Tek_Object.objects.filter(category__name='Высокая').count()
    count_medium = Tek_Object.objects.filter(category__name='Средняя').count()
    count_low = Tek_Object.objects.filter(category__name='Низкая').count()
    news = News.objects.filter(date_start__lte=now).filter(date_end__gte=now).order_by('id').reverse()

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

    context = {
        'count_ul': count_ul,
        'count_all': count_all,
        'count_high': count_high,
        'count_medium': count_medium,
        'count_low': count_low,
        'news': news,
        'count_now_year': count_now_year,
        'count_last_day': count_last_day,
    }
    return render(request, 'homepage/index.html', context)
