from django.shortcuts import render

def index(request):
    context = {

    }
    return render(request, 'vng_stat/index.html', context)