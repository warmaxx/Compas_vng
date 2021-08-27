from django.shortcuts import render
from homepage.models import Region, FedRegion
from phonebook.models import Departament, Contact
from django.db.models import Sum


# Create your views here.
def index(request):
    pass


def pers(request):
    regions = Region.objects.all().order_by('name')
    fed_regions = FedRegion.objects.all().order_by('name')
    info = ''
    select_region_id = '0'
    select_fed_region_id = '0'
    select_region_name = ''
    select_fed_region_name = ''
    count_deps_gk = ''
    count_deps_type_2 = ''
    count_deps_type_3 = ''
    count_deps_type_4 = ''
    count_pers_plan = ''
    count_pers_fact = ''
    count_pers_result = ''
    count_pers_result_percent = ''
    select_stat = 0
    count_pers_work = ''
    count_pers_ill = ''
    count_pers_travel = ''
    count_pers_holiday = ''
    count_pers_pregnant =''
    count_pers_study=''
    count_pers_foreign=''

    if request.method == 'POST':
        try:
            select_stat = request.POST.get('select_stat')
            if select_stat == None:
                select_stat = 0
            if int(select_stat) == 1:
                select_fed_region_name = 'Россия'
                info = 'success'
                count_deps_gk = Departament.objects.filter(type__in=(2, 3, 4)).count()

                count_deps_type_2 = Departament.objects.filter(type=2).count()
                count_deps_type_3 = Departament.objects.filter(type=3).count()
                count_deps_type_4 = Departament.objects.filter(type=4).count()
                count_pers_plan = Departament.objects.filter(type__in=(2, 3, 4)).aggregate(
                    count_employees__sum=Sum('count_employees'))
                count_pers_plan = count_pers_plan['count_employees__sum']
                count_pers_fact = Contact.objects.filter(departament__type__in=(2, 3, 4)).count()
                count_pers_result = count_pers_plan - count_pers_fact
                count_pers_result_percent = round(
                    ((count_pers_plan - count_pers_fact) / count_pers_plan) * 100, 2)
                count_pers_work = Contact.objects.filter(status=0).count()
                count_pers_ill = Contact.objects.filter(status=1).count()
                count_pers_travel = Contact.objects.filter(status=2).count()
                count_pers_holiday = Contact.objects.filter(status=3).count()
                count_pers_pregnant = Contact.objects.filter(status=4).count()
                count_pers_study = Contact.objects.filter(status=5).count()
                count_pers_foreign = Contact.objects.filter(status=6).count()
            if int(select_stat) == 2:

                try:
                    select_fed_region_id = request.POST.get('fed_region_id')
                    select_fed_region_name = FedRegion.objects.filter(id=select_fed_region_id).values_list('name',
                                                                                                           flat=True)
                    select_fed_region_name = select_fed_region_name[0]

                    info = 'success'

                    count_deps_gk = Departament.objects.filter(region__fedname_id=select_fed_region_id).filter(
                        type__in=(2, 3, 4)).count()

                    count_deps_type_2 = Departament.objects.filter(region__fedname_id=select_fed_region_id).filter(
                        type=2).count()
                    count_deps_type_3 = Departament.objects.filter(region__fedname_id=select_fed_region_id).filter(
                        type=3).count()
                    count_deps_type_4 = Departament.objects.filter(region__fedname_id=select_fed_region_id).filter(
                        type=4).count()
                    count_pers_plan = Departament.objects.filter(
                        region__fedname_id=select_fed_region_id).filter(
                        type__in=(2, 3, 4)).aggregate(
                        count_employees__sum=Sum('count_employees'))
                    count_pers_plan = count_pers_plan['count_employees__sum']
                    count_pers_fact = Contact.objects.filter(
                        departament__region__fedname_id=select_fed_region_id).filter(
                        departament__type__in=(2, 3, 4)).count()
                    count_pers_result = count_pers_plan - count_pers_fact
                    count_pers_result_percent = round(
                        ((count_pers_plan - count_pers_fact) / count_pers_plan) * 100, 2)
                    count_pers_work = Contact.objects.filter(status=0).filter(
                        departament__region__fedname_id=select_fed_region_id).count()
                    count_pers_ill = Contact.objects.filter(status=1).filter(
                        departament__region__fedname_id=select_fed_region_id).count()
                    count_pers_travel = Contact.objects.filter(status=2).filter(
                        departament__region__fedname_id=select_fed_region_id).count()
                    count_pers_holiday = Contact.objects.filter(status=3).filter(
                        departament__region__fedname_id=select_fed_region_id).count()
                    count_pers_pregnant = Contact.objects.filter(status=4).filter(
                        departament__region__fedname_id=select_fed_region_id).count()
                    count_pers_study = Contact.objects.filter(status=5).filter(
                        departament__region__fedname_id=select_fed_region_id).count()
                    count_pers_foreign = Contact.objects.filter(status=6).filter(
                        departament__region__fedname_id=select_fed_region_id).count()
                except Exception as e:
                    print(e)
                    info = ''
            if int(select_stat) == 3:
                select_region_id = request.POST.get('region_id')
                select_region_name = Region.objects.filter(id=select_region_id).values_list('name', flat=True)
                select_region_name = select_region_name[0]
                try:
                    info = 'success'
                    count_deps_gk = Departament.objects.filter(region=select_region_id).filter(
                        type__in=(2, 3, 4)).count()
                    count_deps_type_2 = Departament.objects.filter(region=select_region_id).filter(type=2).count()
                    count_deps_type_3 = Departament.objects.filter(region=select_region_id).filter(type=3).count()
                    count_deps_type_4 = Departament.objects.filter(region=select_region_id).filter(type=4).count()
                    count_pers_plan = Departament.objects.values('region').filter(region=select_region_id).filter(
                        type__in=(2, 3, 4)).annotate(
                        Sum('count_employees'))
                    count_pers_plan = count_pers_plan[0]['count_employees__sum']
                    count_pers_fact = Contact.objects.filter(departament__region=select_region_id).filter(
                        departament__type__in=(2, 3, 4)).count()
                    count_pers_result = count_pers_plan - count_pers_fact
                    count_pers_result_percent = round(
                        ((count_pers_plan - count_pers_fact) / count_pers_plan) * 100, 2)
                    count_pers_work = Contact.objects.filter(status=0).filter(departament__region=select_region_id).count()
                    count_pers_ill = Contact.objects.filter(status=1).filter(departament__region=select_region_id).count()
                    count_pers_travel = Contact.objects.filter(status=2).filter(departament__region=select_region_id).count()
                    count_pers_holiday = Contact.objects.filter(status=3).filter(departament__region=select_region_id).count()
                    count_pers_pregnant = Contact.objects.filter(status=4).filter(departament__region=select_region_id).count()
                    count_pers_study = Contact.objects.filter(status=5).filter(departament__region=select_region_id).count()
                    count_pers_foreign = Contact.objects.filter(status=6).filter(departament__region=select_region_id).count()
                except Exception as e:
                    info = ''
                    print(e)
        except Exception as e:
            info = ''
            print(e)

    context = {
        'info': info,
        'regions': regions,
        'fed_regions': fed_regions,
        'select_stat': int(select_stat),
        'select_region_id': int(select_region_id),
        'select_fed_region_id': int(select_fed_region_id),
        'select_region_name': select_region_name,
        'select_fed_region_name': select_fed_region_name,
        'count_deps_gk': count_deps_gk,
        'count_deps_type_2': count_deps_type_2,
        'count_deps_type_3': count_deps_type_3,
        'count_deps_type_4': count_deps_type_4,
        'count_pers_plan': count_pers_plan,
        'count_pers_fact': count_pers_fact,
        'count_pers_result': count_pers_result,
        'count_pers_result_percent': count_pers_result_percent,
        'count_pers_work': count_pers_work,
        'count_pers_ill': count_pers_ill,
        'count_pers_travel': count_pers_travel,
        'count_pers_holiday': count_pers_holiday,
        'count_pers_pregnant':count_pers_pregnant,
        'count_pers_study':count_pers_study,
        'count_pers_foreign':count_pers_foreign,

    }
    return render(request, 'vng_info/index.html', context)
