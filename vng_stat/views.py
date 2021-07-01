from django.shortcuts import render
from homepage.models import FedRegion, Region
from .models import Check, Ul, Tek_Object, Category, Form
import datetime
from django.core.files.storage import FileSystemStorage
import pylightxl as xl
#import os

month = {'Январь': 1,
         'Февраль': 2,
         'Март': 3,
         'Апрель': 4,
         'Май': 5,
         'Июнь': 6,
         'Июль': 7,
         'Август': 8,
         'Сентябрь': 9,
         'Октябрь': 10,
         'Ноябрь': 11,
         'Декабрь': 12
         }


def upload(request):
    upload_file = ''
    success = False
    error = False
    error_list = []
    ul_count = 0
    tek_obj_count = 0
    check_count = 0

    try:
        if request.method == 'POST' and request.FILES['upload_file']:
            myfile = request.FILES['upload_file']
            location = 'vng_stat/xls/'
            fs = FileSystemStorage(location=location)
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            try:
                db = xl.readxl(location + uploaded_file_url)
                for row in db.ws(db.ws_names[0]).rows:
                    if str(row[16]).strip() != 'ul_inn':
                        # Проверка наличия ЮЛ
                        if Ul.objects.filter(INN=str(row[16]).strip()).count() == 0:
                            # Добавление ЮЛ
                            if len(str(row[15]).strip()) != 13:
                                error_list.append('Ошибка в номере ОГРН в строке' + str(row))
                                continue
                            if len((str(row[16])).strip()) != 10:
                                error_list.append('Ошибка в номере ИНН в строке' + str(row))
                                continue
                            else:
                                ul = Ul.objects.create(name=row[13].strip(),
                                                       place=row[14].strip(),
                                                       OGRN=str(row[15]).strip(),
                                                       INN=str(row[16]).strip()
                                                       )
                                ul_count += 1

                        # Проверка наличия объекта
                        if Tek_Object.objects.filter(name=str(row[3]).strip()).filter(place=str(row[4]).strip()).filter(ul__INN=str(row[16]).strip()).count() == 0:
                            ul_id = Ul.objects.get(INN=str(row[16]).strip()).id
                            category_id = Category.objects.get(name=str(row[5]).strip().title()).id
                            region_id = Region.objects.get(name=str(row[1]).strip()).id
                            # Добавление объекта
                            tek = Tek_Object.objects.create(name=str(row[3]).strip(),
                                                            place=str(row[4]).strip(),
                                                            ul_id=ul_id,
                                                            category_id=category_id,
                                                            region_id=region_id
                                                            )
                            tek_obj_count += 1


                        tek_object_id = Tek_Object.objects.get(name=str(row[3]).strip(), place=str(row[4]).strip(), ul__INN=str(row[16]).strip()).id
                        form_id = Form.objects.get(name=str(row[10]).strip().title()).id
                        date_latest_check = None
                        if str(row[6]).strip() == 'Проверка не проводилась':
                            date_latest_check = None
                        if str(row[6]).strip() != 'Проверка не проводилась':
                            date_latest_check = datetime.datetime.strptime(row[6], "%Y/%m/%d")
                        # Добавить перевод месяца в нужный формат
                        d_year = int(datetime.date.today().year)
                        d_month = int(month[str(row[8]).strip()])
                        date_next_check = datetime.date(d_year, d_month, 1)
                        # Добавление проверки
                        check = Check.objects.create(tek_Object_id=tek_object_id,
                                                     date_latest_check=date_latest_check,
                                                     date_next_check=date_next_check,
                                                     duration=row[9],
                                                     form_id=form_id,
                                                     target_text=str(row[11]).strip(),
                                                     target_link=str(row[12]).strip()
                                                     )
                        check_count += 1
            except Exception as e:
                print(e)
            success = True

    except Exception as e:
        success = False
        print(e)

    context = {
        'upload_file': upload_file,
        'success': success,
        'ul_count': ul_count,
        'tek_obj_count': tek_obj_count,
        'check_count': check_count,
        'error': error,
        'error_list': error_list,
        'len_error_list': len(error_list),
    }
    return render(request, 'vng_stat/upload.html', context)


def index(request):
    checks = Check.objects.all().values(
        'tek_Object__region__name',
        'tek_Object__region__fedname__name',
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
    now_year = datetime.datetime.today().year
    now_month = datetime.datetime.today().month
    now_date = datetime.date.today()
    # Вывод по РФ
    tr += (
            '<tr style="background: bisque">'
            '<td>ВСЕГО за РФ</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).values('tek_Object__ul__INN').distinct().count()) + ' </td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(form__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(form__id='1').count()) + '</td>'
            '<td>' + str(checks.filter(date_latest_check__year=None).count()) +'</td>'
            '<td>' + str(checks.filter(date_latest_check__year=now_year-1).count()) +'</td>'
            '<td>' + str(checks.filter(date_latest_check__year=now_year-2).count()) +'</td>'
            '<td>' + str(checks.filter(date_latest_check__year__lt= now_year-2).count()) +'</td>'
                                                                                                            
            # Январь                                                                                           
            '<td>' + str(checks.filter(date_next_check__month='01').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='01').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='01').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='01').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='01').filter(date_next_check__year=now_year).count()) + '</td>'
            
            # Февраль
            '<td>' + str(checks.filter(date_next_check__month='02').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='02').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='02').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='02').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='02').filter(date_next_check__year=now_year).count()) + '</td>'
            
            # Март
            '<td>' + str(checks.filter(date_next_check__month='03').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='03').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='03').filter(date_next_check__year=now_year).count()) + '</td>'
                                                                                                                                                               
            # Апрель
            '<td>' + str(checks.filter(date_next_check__month='04').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='04').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='04').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='04').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='04').filter(date_next_check__year=now_year).count()) + '</td>'
            
            # Май
            '<td>' + str(checks.filter(date_next_check__month='05').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='05').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='05').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='05').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='05').filter(date_next_check__year=now_year).count()) + '</td>'
                                                                                                                                                               
            # Июнь
            '<td>' + str(checks.filter(date_next_check__month='06').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='06').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='06').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='06').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='06').filter(date_next_check__year=now_year).count()) + '</td>'
                                                                                                                                                               
            # Июль
            '<td>' + str(checks.filter(date_next_check__month='07').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='07').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='07').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='07').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='07').filter(date_next_check__year=now_year).count()) + '</td>'
            
            # Август
            '<td>' + str(checks.filter(date_next_check__month='08').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='08').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='08').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='08').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='08').filter(date_next_check__year=now_year).count()) + '</td>'                                                                                                                                                   
            
            # Сентябрь
            '<td>' + str(checks.filter(date_next_check__month='09').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='09').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='09').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='09').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='09').filter(date_next_check__year=now_year).count()) + '</td>'
                                                                                                                                                               
            # Октябрь
            '<td>' + str(checks.filter(date_next_check__month='10').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='10').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='10').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='10').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='10').filter(date_next_check__year=now_year).count()) + '</td>'
                                                                                                                                                               
            # Ноябрь
            '<td>' + str(checks.filter(date_next_check__month='11').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='11').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='11').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='11').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='11').filter(date_next_check__year=now_year).count()) + '</td>'
                                                                                                                                                               
            # Декабрь
            '<td>' + str(checks.filter(date_next_check__month='12').filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='12').filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='12').filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month='12').filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month='12').filter(date_next_check__year=now_year).count()) + '</td>'
            
            # Итого
            '<td>' + str(checks.filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).count()) + '</td>'                                                                                                                                                   
            
            '</tr>'
    )
    for f in fedregions:
        # Вывод по Округам
        tr += (
            '<tr style="background: aliceblue">'
            '<td>'+str(f['name'])+'</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().count()) + ' </td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(form__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(form__id='1').count()) + '</td>'
            '<td>' + str(checks.filter(date_latest_check__year=None).filter(tek_Object__region__fedname=f['id']).count()) +'</td>'
            '<td>' + str(checks.filter(date_latest_check__year=now_year-1).filter(tek_Object__region__fedname=f['id']).count()) +'</td>'
            '<td>' + str(checks.filter(date_latest_check__year=now_year-2).filter(tek_Object__region__fedname=f['id']).count()) +'</td>'
            '<td>' + str(checks.filter(date_latest_check__year__lt=now_year-2).filter(tek_Object__region__fedname=f['id']).count()) +'</td>'
                                                                                                            
            # Январь                                                                                           
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='01').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='01').count()) + '</td>'
            
            # Февраль
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='02').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='02').count()) + '</td>'
            
            # Март
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='03').count()) + '</td>'
                                                                                                                                                               
            # Апрель
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='04').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='04').count()) + '</td>'
            
            # Май
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='05').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='05').count()) + '</td>'
                                                                                                                                                               
            # Июнь
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='06').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='06').count()) + '</td>'
                                                                                                                                                               
            # Июль
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='07').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='07').count()) + '</td>'
            
            # Август
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='08').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='08').count()) + '</td>'                                                                                                                                                   
            
            # Сентябрь
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='09').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='09').count()) + '</td>'
                                                                                                                                                               
            # Октябрь
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='10').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='10').count()) + '</td>'
                                                                                                                                                               
            # Ноябрь
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='11').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='11').count()) + '</td>'
                                                                                                                                                               
            # Декабрь
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='12').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='3').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='2').count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='1').count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).distinct().filter(date_next_check__month='12').count()) + '</td>'
            
            # Итого 
            '<td>' + str(checks.filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).filter(tek_Object__category__id='3').filter(tek_Object__region__fedname=f['id']).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).filter(tek_Object__category__id='2').filter(tek_Object__region__fedname=f['id']).count()) + '</td>'
            '<td>' + str(checks.filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).filter(tek_Object__category__id='1').filter(tek_Object__region__fedname=f['id']).count()) + '</td>'
            '<td>' + str(checks.values('tek_Object__ul__INN').distinct().filter(date_next_check__month__gte='01').filter(date_next_check__month__lte=now_month).filter(date_next_check__year=now_year).filter(tek_Object__region__fedname=f['id']).count()) + '</td>'                                                                                                                                                   
            
            '</tr>'
        )

        for r in regions.filter(fedname_id=f['id']):
            # Вывод по регионам
            tr += (
            '<tr>'
                '<td>' + str(r['name']) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().count()) + ' </td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(form__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(form__id='1').count()) + '</td>'
                '<td>' + str(checks.filter(date_latest_check__year=None).filter(tek_Object__region__id=r['id']).count()) +'</td>'
                '<td>' + str(checks.filter(date_latest_check__year=now_year-1).filter(tek_Object__region__id=r['id']).count()) +'</td>'
                '<td>' + str(checks.filter(date_latest_check__year=now_year-2).filter(tek_Object__region__id=r['id']).count()) +'</td>'
                '<td>' + str(checks.filter(date_latest_check__year__lt=now_year-2).filter(tek_Object__region__id=r['id']).count()) +'</td>'
                
                # Январь                                                                                           
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='01').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='01').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='01').count()) + '</td>'
                
                # Февраль
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='02').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='02').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='02').count()) + '</td>'
                
                # Март
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='03').count()) + '</td>'
                                                                                                                                                                   
                # Апрель
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='04').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='04').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='04').count()) + '</td>'
                
                # Май
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='05').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='05').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='05').count()) + '</td>'
                                                                                                                                                                   
                # Июнь
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='06').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='06').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='06').count()) + '</td>'
                                                                                                                                                                   
                # Июль
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='07').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='07').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='07').count()) + '</td>'
                
                # Август
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='08').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='08').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='08').count()) + '</td>'                                                                                                                                                   
                
                # Сентябрь
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='09').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='09').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='09').count()) + '</td>'
                                                                                                                                                                   
                # Октябрь
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='10').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='10').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='10').count()) + '</td>'
                                                                                                                                                                   
                # Ноябрь
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='11').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='11').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='11').count()) + '</td>'
                                                                                                                                                                   
                # Декабрь
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='12').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='12').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='12').count()) + '</td>'
                
                # Итого (доделать)
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='3').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='2').count()) + '</td>'
                '<td>' + str(checks.filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).filter(date_next_check__month='03').filter(tek_Object__category__id='1').count()) + '</td>'
                '<td>' + str(checks.values('tek_Object__ul__INN').filter(date_next_check__year=now_year).filter(tek_Object__region__id=r['id']).distinct().filter(date_next_check__month='03').count()) + '</td>'                                                                                                                                                   
                
            ' </tr>'
            )

    context = {
        'now_year': now_year,
        'now_year_1': now_year - 1,
        'now_year_2': now_year - 2,
        'now_date': now_date,
        'tr': tr,

        'fedregions': fedregions,
        'regions': regions,
    }
    return render(request, 'vng_stat/stat.html', context)
