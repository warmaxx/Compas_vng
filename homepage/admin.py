from django.contrib import admin

# Register your models here.
from .models import FedRegion, Region

admin.site.register(FedRegion)
admin.site.register(Region)
admin.site.site_header = 'Администрирование Системы'
admin.site.site_title = 'ИС ВНГ ГК'
