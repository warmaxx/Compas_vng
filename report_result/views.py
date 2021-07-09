from report_result.models import Modul_1_1, Modul_1_2, Modul_3, Modul_4_1, Modul_4_2, Modul_5, Modul_6, Modul_7, Modul_8
from docxtpl import DocxTemplate
from datetime import datetime, timedelta
from django.http import FileResponse
from Gastroler.settings import BASE_DIR

import os
import locale


def get_date(date):
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('-')
    return (str(date_list[0]) + ' ' +
            str(month_list[int(date_list[1]) - 1]) + ' ' +
            str(date_list[2]) + ' года')


def index(request):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    now = datetime.now()
    now_day = now.day
    now_month = month_list[now.month]
    now_year = now.year
    now_week = now.isocalendar()[1]

    monday = datetime.strptime(f'{now_year}-{now_week}-1', "%Y-%W-%w").date()
    monday.strftime("%d-%m-%Y")
    monday_ru = monday.strftime('%d-%m-%Y')
    sunday = monday + timedelta(days=6.9)
    sunday_ru = sunday.strftime('%d-%m-%Y')

    doc_input_url = os.path.join(BASE_DIR, 'report_result/test_template.docx')
    doc_output_url = os.path.join(BASE_DIR, 'report_result/generated_doc.docx')
    # doc_input_url = '/home/warmaxx/Gastroler/report_result/test_template.docx'
    # doc_output_url = '/home/warmaxx/Gastroler/report_result/generated_doc.docx'
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
