from django.shortcuts import render
from vng_stat.models import Tek_Object, Ul
from news.models import News
from datetime import datetime as dt


def index(request):
    now = dt.now()
    count_ul = Ul.objects.count()
    count_all = Tek_Object.objects.count()
    count_high = Tek_Object.objects.filter(category__name='Высокая').count()
    count_medium = Tek_Object.objects.filter(category__name='Средняя').count()
    count_low = Tek_Object.objects.filter(category__name='Низкая').count()
    news = News.objects.filter(date_start__lte=now).filter(date_end__gte=now).order_by('id').reverse()

    context = {
        'count_ul': count_ul,
        'count_all': count_all,
        'count_high': count_high,
        'count_medium': count_medium,
        'count_low': count_low,
        'news': news,
    }
    return render(request, 'homepage/index.html', context)
