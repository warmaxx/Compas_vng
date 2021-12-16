from django.contrib import admin

# Register your models here.
from .models import FedRegion, Region


class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "fedname", "timezone",)
    search_fields = ("name",)
    list_filter = ("fedname",)
    empty_value_display = "-пусто-"


class FedRegionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(FedRegion, FedRegionAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.site_header = 'Администрирование Системы'
admin.site.site_title = 'ИС ВНГ ГК'
