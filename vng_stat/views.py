from django.shortcuts import render
from homepage.models import FedRegion, Region
from .models import Check
import datetime


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
        'form_id',
        'target_link',
        'target_text',
        'tek_Object__ul__name',
        'tek_Object__ul__place',
        'tek_Object__ul__OGRN',
        'tek_Object__ul__INN'
    )
    fedregions = FedRegion.objects.all().values('id', 'name')
    regions = Region.objects.all().values('id', 'name')
    tr = ''
    # Вывод по РФ
    tr += (
            '<tr style="background: bisque">'
            '<td>ВСЕГО за РФ</td>'
            '<td>' + str(checks.count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__category__id='1').count()) + '</td>'
            '<td> ' +str(checks.values('tek_Object__ul__INN').distinct().count()) + ' </td>'
            '<td>' + str(checks.filter(form__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(form__id='1').count()) + '</td>'
            '<td>не проводилась</td>'
            '<td>2019</td>'
            '<td>2018</td>'
            '<td>более ранее сроки</td>'
                                                                                                            
            # Январь                                                                                           
            '<td>' + str(checks.filter(date_next_check__month='01').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='01').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='01').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='01').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='01').count()) + '</td>'
            
            # Февраль
            '<td>' + str(checks.filter(date_next_check__month='02').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='02').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='02').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='02').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='02').count()) + '</td>'
            
            # Март
            '<td>' + str(checks.filter(date_next_check__month='03').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='03').count()) + '</td>'
                                                                                                                                                               
            # Апрель
            '<td>' + str(checks.filter(date_next_check__month='04').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='04').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='04').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='04').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='04').count()) + '</td>'
            
            # Май
            '<td>' + str(checks.filter(date_next_check__month='05').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='05').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='05').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='05').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='05').count()) + '</td>'
                                                                                                                                                               
            # Июнь
            '<td>' + str(checks.filter(date_next_check__month='06').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='06').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='06').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='06').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='06').count()) + '</td>'
                                                                                                                                                               
            # Июль
            '<td>' + str(checks.filter(date_next_check__month='07').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='07').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='07').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='07').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='07').count()) + '</td>'
            
            # Август
            '<td>' + str(checks.filter(date_next_check__month='08').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='08').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='08').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='08').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='08').count()) + '</td>'                                                                                                                                                   
            
            # Сентябрь
            '<td>' + str(checks.filter(date_next_check__month='09').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='09').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='09').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='09').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='09').count()) + '</td>'
                                                                                                                                                               
            # Октябрь
            '<td>' + str(checks.filter(date_next_check__month='10').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='10').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='10').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='10').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='10').count()) + '</td>'
                                                                                                                                                               
            # Ноябрь
            '<td>' + str(checks.filter(date_next_check__month='11').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='11').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='11').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='11').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='11').count()) + '</td>'
                                                                                                                                                               
            # Декабрь
            '<td>' + str(checks.filter(date_next_check__month='12').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='12').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='12').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='12').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='12').count()) + '</td>'
            
            # Итого (доделать)
            '<td>' + str(checks.filter(date_next_check__month='03').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='03').count()) + '</td>'                                                                                                                                                   
            
            '</tr>'
    )
    for f in fedregions:
        # Вывод по Округам
        tr+= (
            '<tr style="background: aliceblue">'
            '<td>'+str(f['name'])+'</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname =f['id']).count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td> ' +str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().count()) + ' </td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(form__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(form__id='1').count()) + '</td>'
            '<td>не проводилась</td>'
            '<td>2019</td>'
            '<td>2018</td>'
            '<td>более ранее сроки</td>'
                                                                                                            
            # Январь                                                                                           
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='01').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='01').count()) + '</td>'
            
            # Февраль
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='02').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='02').count()) + '</td>'
            
            # Март
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='03').count()) + '</td>'
                                                                                                                                                               
            # Апрель
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='04').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='04').count()) + '</td>'
            
            # Май
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='05').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='05').count()) + '</td>'
                                                                                                                                                               
            # Июнь
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='06').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='06').count()) + '</td>'
                                                                                                                                                               
            # Июль
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='07').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='07').count()) + '</td>'
            
            # Август
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='08').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='08').count()) + '</td>'                                                                                                                                                   
            
            # Сентябрь
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='09').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='09').count()) + '</td>'
                                                                                                                                                               
            # Октябрь
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='10').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='10').count()) + '</td>'
                                                                                                                                                               
            # Ноябрь
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='11').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='11').count()) + '</td>'
                                                                                                                                                               
            # Декабрь
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='12').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='12').count()) + '</td>'
            
            # Итого (доделать)
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='03').count()) + '</td>'                                                                                                                                                   
            
            '</tr>'
        )

        for r in regions.filter(fedname_id=f['id']):
            # Вывод по регионам
            tr += (
            '<tr>'
                '<td>' + str(r['name']) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(tek_Object__category__id='1').count()) + '</td>'
                '<td> ' +str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().count()) + ' </td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(form__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(form__id='1').count()) + '</td>'
                '<td>не проводилась</td>'
                '<td>2019</td>'
                '<td>2018</td>'
                '<td>более ранее сроки</td>'
                
                # Январь                                                                                           
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='01').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='01').count()) + '</td>'
                
                # Февраль
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='02').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='02').count()) + '</td>'
                
                # Март
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='03').count()) + '</td>'
                                                                                                                                                                   
                # Апрель
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='04').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='04').count()) + '</td>'
                
                # Май
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='05').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='05').count()) + '</td>'
                                                                                                                                                                   
                # Июнь
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='06').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='06').count()) + '</td>'
                                                                                                                                                                   
                # Июль
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='07').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='07').count()) + '</td>'
                
                # Август
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='08').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='08').count()) + '</td>'                                                                                                                                                   
                
                # Сентябрь
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='09').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='09').count()) + '</td>'
                                                                                                                                                                   
                # Октябрь
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='10').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='10').count()) + '</td>'
                                                                                                                                                                   
                # Ноябрь
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='11').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='11').count()) + '</td>'
                                                                                                                                                                   
                # Декабрь
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='12').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='12').count()) + '</td>'
                
                # Итого (доделать)
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='03').count()) + '</td>'                                                                                                                                                   
                
            ' </tr>'
            )

    context = {

        'tr': tr,
        'checks': checks,
        'fedregions': fedregions,
        'regions': regions,
    }
    return render(request, 'vng_stat/stat.html', context)
