from django.shortcuts import render


def index(request):
    context = {

    }

    return render(request, 'vng_incidents/index.html', context)
