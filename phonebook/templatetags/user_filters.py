from django import template
from datetime import datetime as dt

# В template.Library зарегистрированы все теги и фильтры шаблонов
# добавляем к ним и наш фильтр
register = template.Library()


@register.filter
def now_time(delta_time):
    now = dt.utcnow()
    new_time_h = (now.hour + int(delta_time)) % 24
    new_time_m = str(0) + str(now.minute)

    return str(new_time_h) + ':' + str(new_time_m[-2:])
