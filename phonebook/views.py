from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Contact, Departament
from homepage.models import FedRegion, Region, Job, Rank, STATUS_CONTACT_CHOICES
from django.http import JsonResponse
from datetime import datetime as dt


def index(request):
    contacts = Contact.objects.all()
    fed_regions = FedRegion.objects.all()
    regions = Region.objects.all()
    jobs = Job.objects.all()
    ranks = Rank.objects.all()
    deps = Departament.objects.all()
    now = dt.utcnow()
    persons = False
    search_name = ''
    if request.POST.get('search_name'):
        search_name = request.POST.get('search_name')
        persons = contacts.filter(sur_name__icontains=search_name)
    delim = ";"
    distinct_emails = ''
    all_emails = ''
    all_ground_emails = ''
    email_list = list(Contact.objects.filter(departament__type=1, status=0).values_list('email', flat=True))
    for email in email_list:
        distinct_emails = distinct_emails + str(email) + delim

    email_list = list(Contact.objects.filter(status=0).values_list('email', flat=True))
    for email in email_list:
        all_emails = all_emails + str(email) + delim

    email_list = list(Contact.objects.filter(status=0).exclude(departament__type=1).values_list('email', flat=True))
    for email in email_list:
        all_ground_emails = all_ground_emails + str(email) + delim

    context = {
        'contacts': contacts,
        'fed_regions': fed_regions,
        'regions': regions,
        'jobs': jobs,
        'ranks': ranks,
        'deps': deps,
        'distinct_emails': distinct_emails,
        'all_emails': all_emails,
        'all_ground_emails': all_ground_emails,
        'search_name': search_name,
        'persons': persons,
        'now_h': now.hour,
        'now_m': now.minute,
    }
    return render(request, 'phonebook/index.html', context)


@csrf_exempt
def deps(request, *args, **kwargs):
    data = request.POST
    limit = data.get('pagination[perpage]', 10)
    offset = data.get('pagination[page]', 0)
    departs = Departament.objects.order_by('position')
    if data.get('query[generalSearch]'):
        query = data.get('query[generalSearch]')
        departs = departs.filter(contact__sur_name__icontains=str(query))
    count = departs.count()
    meta_data = {}
    meta_data['page'] = data.get('pagination[page]')
    pages = int(count) // int(limit)
    meta_data['pages'] = int(pages)
    meta_data['perpage'] = int(limit)
    meta_data['total'] = int(count)
    meta_data['sort'] = 'asc'
    meta_data['field'] = 'RecordID'

    j = []
    jdeps = {}

    for depart in departs:
        jdata = {}
        jdata['RecordID'] = depart.pk
        jdata['name'] = depart.name
        jdata['region_name'] = depart.region.name
        jdata['address'] = depart.address
        jdata['time'] = depart.region.timezone
        delim = ";"
        jdata['emails'] = ''
        email_list = list(Contact.objects.filter(departament=depart, status=0).values_list('email', flat=True))
        for email in email_list:
            jdata['emails'] = jdata['emails'] + str(email) + delim
        # jdata['emails'] = list(Contact.objects.filter(departament=depart).values_list('email', flat=True))
        j.append(jdata)
    jdeps['meta'] = meta_data
    jdeps['data'] = j
    return JsonResponse(jdeps)


@csrf_exempt
def pers(request, *args, **kwargs):
    data = request.POST
    deps_id = data.get('query[CustomerID]')
    contacts = Contact.objects.filter(departament_id=deps_id)
    contacts = contacts.order_by('job__position','rank__position', 'sur_name', 'name')
    limit = data.get('pagination[perpage]', 10)
    offset = data.get('pagination[page]', 0)
    count = contacts.count()
    meta_data = {}
    meta_data['page'] = data.get('pagination[page]')
    pages = int(count) // int(limit)
    meta_data['pages'] = int(pages)
    meta_data['perpage'] = int(limit)
    meta_data['total'] = int(count)
    meta_data['sort'] = 'asc'
    meta_data['field'] = 'RecordID'
    j = []
    jpers = {}

    for contact in contacts:
        jdata = {}
        jdata['RecordID'] = contact.pk
        jdata['name'] = (
                str(contact.sur_name)
                + ' ' + str(contact.name)
                + ' ' + str(contact.patronymic)
        )
        jdata['rank'] = contact.rank.short_name
        jdata['job'] = contact.job.short_name
        jdata['work_phone'] = contact.work_phone
        jdata['cell_phone'] = contact.cell_phone
        jdata['email'] = contact.email
        jdata['comment'] = contact.comment
        jdata['status'] = contact.status
        jdata['time'] = contact.departament.region.timezone
        j.append(jdata)
    jpers['meta'] = meta_data
    jpers['data'] = j
    return JsonResponse(jpers)


@csrf_exempt
def change_status(request, *args, **kwargs):
    contact = Contact.objects.get(id=kwargs['pers_id'])
    status = STATUS_CONTACT_CHOICES[kwargs['status_id']]
    contact.status = status[0]
    contact.save()
    return redirect('/phonebook/')


@csrf_exempt
def change_comment(request, *args, **kwargs):
    contact = Contact.objects.get(id=kwargs['pers_id'])
    contact.comment = kwargs['comment']
    contact.save()
    return redirect('/phonebook/')
