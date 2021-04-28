from django.shortcuts import render
from homepage.models import FedRegion, Region
from .models import Check, Tek_Object, Ul, Form, Category


def index(request):
    checks = Check.objects.all().values(
        'tek_Object__region__name',
        'tek_Object__region__fedname',
        'id',
        'tek_Object__name',
        'tek_Object__place',
        'tek_Object__category__name',
        'date_latest_check',
        'date_next_check',
        'duration',
        'form__name',
        'target_link',
        'target_text',
        'tek_Object__ul__name',
        'tek_Object__ul__place',
        'tek_Object__ul__OGRN',
        'tek_Object__ul__INN'
    )

    context = {

        'checks': checks,
    }

    return render(request, 'vng_stat/index.html', context)


def stat(request):
    checks = Check.objects.all().values(
        'tek_Object__region__name',
        'tek_Object__region__fedname',
        'id',
        'tek_Object__name',
        'tek_Object__place',
        'tek_Object__category__name',
        'date_latest_check',
        'date_next_check',
        'duration',
        'form__name',
        'target_link',
        'target_text',
        'tek_Object__ul__name',
        'tek_Object__ul__place',
        'tek_Object__ul__OGRN',
        'tek_Object__ul__INN'
    )
    fedregions = FedRegion.objects.all().values('id', 'name')
    regions = Region.objects.all().values('id', 'name')
    p = checks.filter(tek_Object__category__name='Низкий').count()
    context = {
        'p':p,
        'checks': checks,
        'fedregions': fedregions,
        'regions': regions,
    }
    return render(request, 'vng_stat/stat.html', context)
