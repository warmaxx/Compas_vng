from django.shortcuts import render
from .models import Contact, Status
from homepage.models import FedRegion, Region, Job, Rank, Departament

def index(request):
    contacts = Contact.objects.all()
    fed_regions = FedRegion.objects.all()
    regions = Region.objects.all()

    context = {
        'contacts': contacts,
        'fed_regions': fed_regions,
        'regions': regions,
    }

    return render(request, 'phonebook/index.html', context)
