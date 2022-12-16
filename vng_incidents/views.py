from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http import JsonResponse
import datetime as dt

from vng_incidents.models import Incident
from homepage.models import Region


def index(request):
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
    regions = Region.objects.all()
    context = {
        'incidents': incidents,
        'regions': regions,
        'count_now_year': count_now_year,
        'count_last_day': count_last_day,
    }

    return render(request, 'vng_incidents/index.html', context)


@csrf_exempt
def incs(request, *args, **kwargs):
    data = request.POST
    print(data)
    dates = data['columns[5][search][value]']
    region = data['columns[2][search][value]']
    inc_id = data['columns[0][search][value]']
    subject = data['columns[4][search][value]']
    source = data['columns[6][search][value]']
    start = int(data['start'])
    length = int(data['length'])
    if len(dates) > 0:
        date_start, date_end = str(dates).split('|')
    else:
        date_start = '01-01-1900'
        date_end = '01-01-2900'
    date_start = dt.datetime.strptime(date_start, "%d-%m-%Y")
    date_end = dt.datetime.strptime(date_end, "%d-%m-%Y")

    limit = data.get('pagination[perpage]', 10)
    offset = data.get('pagination[page]', 0)
    incidents = Incident.objects.filter(Q(date_time__gte=date_start),
                                        Q(date_time__lte=date_end + dt.timedelta(days=1))).order_by('-date_time')
    if len(region) > 0:
        incidents = incidents.filter(region_id=region)
    if len(inc_id) > 0:
        incidents = incidents.filter(id=inc_id)
    if len(subject) > 0:
        incidents = incidents.filter(subject=subject)
    if len(source) > 0:
        incidents = incidents.filter(source=source)

    count = incidents.count()
    meta_data = {}
    meta_data['page'] = data.get('pagination[page]')
    pages = int(count) // int(length)
    meta_data['pages'] = int(pages)
    meta_data['perpage'] = int(length)
    meta_data['total'] = int(count)
    meta_data['sort'] = 'asc'
    meta_data['field'] = 'RecordID'
    j = []
    jinc = {}

    for incident in incidents:
        jdata = {}
        jdata['RecordID'] = incident.pk
        jdata['date_time'] = incident.date_time.strftime('%d-%m-%Y')
        jdata['region'] = incident.region.name
        jdata['source'] = incident.source
        jdata['subject'] = incident.subject
        jdata['inc_text'] = incident.inc_text
        jdata['result'] = incident.result
        jdata['comment'] = incident.comment

        j.append(jdata)
    jinc['meta'] = meta_data
    jinc['recordsTotal'] = count
    jinc['recordsFiltered'] = count
    jinc['data'] = j
    return JsonResponse(jinc)
