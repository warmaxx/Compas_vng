from docxtpl import DocxTemplate
from datetime import datetime, timedelta
from django.http import FileResponse
from django.shortcuts import render
from Gastroler.settings import BASE_DIR
from report_result.models import Modul_1_1, Modul_1_2, Modul_3, Modul_4_1, Modul_4_2, Modul_5, Modul_6, Modul_7, Modul_8

import os
import locale


def inject_today_date():
    return {'today_date': datetime.today()}


def get_date(date):
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('-')
    return (str(date_list[0]) + ' ' +
            str(month_list[int(date_list[1]) - 1]) + ' ' +
            str(date_list[2]) + ' года')


def index(request):
    res_modul1_1 = False
    res_modul1_2 = False
    res_modul3 = False
    res_modul4_1 = False
    res_modul4_2 = False
    res_modul5 = False
    res_modul6 = False
    res_modul7 = False
    res_modul8 = False

    person = ''
    input_no = ''
    output_no = ''
    text = ''
    if request.POST:
        person = request.POST.get('person')
        input_no = request.POST.get('input_no')
        output_no = request.POST.get('output_no')
        text = request.POST.get('text')
        if person == '' and input_no == '' and output_no == '' and text == '':
            context = {
                'start_date': datetime.strftime(datetime.today(), '%Y-%m-%d'),
                'end_date': datetime.strftime(datetime.today(), '%Y-%m-%d'),
            }
            return render(request, 'result_report/index.html', context)
        print(request.POST)
        if text != '':
            res_modul1_1 = Modul_1_1.objects.order_by('date').values_list('date', flat=True)
            res_modul1_2 = Modul_1_2.objects.order_by('date').values_list('date', flat=True)
            res_modul3 = Modul_3.objects.order_by('date').values_list('date', flat=True)
            res_modul4_1 = Modul_4_1.objects.order_by('date').values_list('date', flat=True)
            res_modul4_2 = Modul_4_2.objects.order_by('date').values_list('date', flat=True)
            res_modul5 = Modul_5.objects.order_by('date').values_list('date', flat=True)
            res_modul6 = Modul_6.objects.order_by('date').values_list('date', flat=True)
            res_modul7 = Modul_7.objects.order_by('date').values_list('date', flat=True)
            res_modul8 = Modul_8.objects.order_by('date').values_list('date', flat=True)

        if person != '' or input_no != '' or output_no != '':
            res_modul1_1 = Modul_1_1.objects.order_by('date').values_list('date', flat=True)
            res_modul1_2 = Modul_1_2.objects.order_by('date').values_list('date', flat=True)

        if len(person) > 0:
            res_modul1_1 = res_modul1_1.filter(person__icontains=str(person))
            res_modul1_2 = res_modul1_2.filter(person__icontains=str(person))
        if len(input_no) > 0:
            res_modul1_1 = res_modul1_1.filter(input_number__icontains=str(input_no))
            res_modul1_2 = res_modul1_2.filter(input_number__icontains=str(input_no))
        if len(output_no) > 0:
            res_modul1_1 = res_modul1_1.filter(output_number__icontains=str(output_no))
            res_modul1_2 = res_modul1_2.filter(output_number__icontains=str(output_no))
        if len(text) > 0:

            res_modul1_1 = res_modul1_1.filter(text__icontains=str(text))
            res_modul1_2 = res_modul1_2.filter(text__icontains=str(text))
            res_modul3 = res_modul3.filter(text__icontains=str(text))
            res_modul4_1 = res_modul4_1.filter(text__icontains=str(text))
            res_modul4_2 = res_modul4_2.filter(text__icontains=str(text))
            res_modul5 = res_modul5.filter(text__icontains=str(text))
            res_modul6 = res_modul6.filter(text__icontains=str(text))
            res_modul7 = res_modul7.filter(text__icontains=str(text))
            res_modul8 = res_modul8.filter(text__icontains=str(text))

            res_modul3 = res_modul3.distinct()
            res_modul4_1 = res_modul4_1.distinct()
            res_modul4_2 = res_modul4_2.distinct()
            res_modul5 = res_modul5.distinct()
            res_modul6 = res_modul6.distinct()
            res_modul7 = res_modul7.distinct()
            res_modul8 = res_modul8.distinct()

        res_modul1_1 = res_modul1_1.distinct()
        res_modul1_2 = res_modul1_2.distinct()

    context = {
        'start_date': datetime.strftime(datetime.today(), '%Y-%m-%d'),
        'end_date': datetime.strftime(datetime.today(), '%Y-%m-%d'),
        'res_modul1_1': res_modul1_1,
        'res_modul1_2': res_modul1_2,
        'res_modul3': res_modul3,
        'res_modul4_1': res_modul4_1,
        'res_modul4_2': res_modul4_2,
        'res_modul5': res_modul5,
        'res_modul6': res_modul6,
        'res_modul7': res_modul7,
        'res_modul8': res_modul8,
        'person': person,
        'input_no': input_no,
        'output_no': output_no,
        'text': text,
    }
    return render(request, 'result_report/index.html', context)


def week(request):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    now = datetime.now()
    now_day = now.day
    now_month = month_list[now.month - 1]
    now_year = now.year
    now_week = now.isocalendar()[1]
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    # monday = datetime.strptime(f'{now_year}-{now_week}-1', "%Y-%W-%w").date()
    monday = datetime.strptime(start_date, "%Y-%m-%d").date()
    monday.strftime("%d-%m-%Y")
    monday_ru = monday.strftime('%d-%m-%Y')
    # sunday = monday + timedelta(days=6.9)
    sunday = datetime.strptime(end_date, "%Y-%m-%d").date()
    sunday_ru = sunday.strftime('%d-%m-%Y')

    doc_input_url = os.path.join(BASE_DIR, 'report_result/test_template.docx')
    doc_output_url = os.path.join(BASE_DIR, 'report_result/generated_doc.docx')
    doc = DocxTemplate(doc_input_url)

    elements_1_1 = Modul_1_1.objects.filter(date__range=(monday, sunday)).order_by('name_from')
    elements_1_2 = Modul_1_2.objects.filter(date__range=(monday, sunday)).order_by('name_from')
    elements_3 = Modul_3.objects.filter(date__range=(monday, sunday))
    elements_4_1 = Modul_4_1.objects.filter(date__range=(monday, sunday))
    elements_4_2 = Modul_4_2.objects.filter(date__range=(monday, sunday))
    elements_5 = Modul_5.objects.filter(date__range=(monday, sunday))
    elements_6 = Modul_6.objects.filter(date__range=(monday, sunday))
    elements_7 = Modul_7.objects.filter(date__range=(monday, sunday))
    elements_8 = Modul_8.objects.filter(date__range=(monday, sunday))
    context = {
        'date_start': get_date(str(monday_ru)),
        'date_end': get_date(str(sunday_ru)),
        'elements_1_1': elements_1_1,
        'elements_1_2': elements_1_2,
        'elements_3': elements_3,
        'elements_4_1': elements_4_1,
        'elements_4_2': elements_4_2,
        'elements_5': elements_5,
        'elements_6': elements_6,
        'elements_7': elements_7,
        'elements_8': elements_8,
        'now_day': now_day,
        'now_month': now_month,
        'now_year': now_year,
    }
    doc.render(context)
    doc.save(doc_output_url)

    return FileResponse(open(doc_output_url, 'rb'))
