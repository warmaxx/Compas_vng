from django.contrib import admin

# Register your models here.
from vng_info.models import TekInfo


class TekInfoAdmin(admin.ModelAdmin):
    list_display = (
    "region", "tek_high", "tek_mid", "tek_low", "vo_deps_foiv", "vo_deps_ul", "vo_deps_ul_special", "vo_pers_vo",
    "vo_pers_special", "vo_obj_vo", "vo_obj_special", "vo_guns_army", "vo_guns_work", "vo_guns_civil", "vo_guns_study",)
    search_fields = ("region__name",)
    empty_value_display = "-пусто-"


admin.site.register(TekInfo, TekInfoAdmin)
