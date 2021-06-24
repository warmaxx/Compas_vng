from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Incident
from phonebook.models import Contact
from django.http import JsonResponse


def index(request):
    incidents = Incident.objects.all()
    context = {
        'incidents': incidents,
    }

    return render(request, 'vng_incidents/index.html', context)


@csrf_exempt
def incs(request, *args, **kwargs):
    data = request.POST
    deps_id = data.get('query[CustomerID]')
    contacts = Contact.objects.filter(departament_id=deps_id)
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
