from django.shortcuts import render
from homepage.models import FedRegion, Region
from .models import Check, Tek_Object, Ul, Form, Category

def index(request):

    checks = Check.objects.all()

    context = {

        'checks': checks,
    }

    return render(request, 'vng_stat/index.html', context)

def stat (request):

    checks = Check.objects.all()
    fedregions = FedRegion.objects.all()
    regions = Region.objects.all()

    p = checks.count()


    context = {
        'p':p,
        'checks': checks,
        'fedregions':fedregions,
        'regions':regions,
    }
    return render(request, 'vng_stat/stat.html', context)

