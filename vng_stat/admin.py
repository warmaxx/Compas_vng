from django.contrib import admin

# Register your models here.
from .models import Check, Category, Ul, Tek_Object, Form


class CheckAdmin(admin.ModelAdmin):
    list_display = ("tek_Object", "date_latest_check", "date_next_check", "duration", "form", "target_text", "target_link")
    list_filter = ("form", "date_next_check")
    empty_value_display = "-пусто-"


class UlAdmin(admin.ModelAdmin):
    list_display = ("name", "place", "INN", "OGRN")
    search_fields = ("name", "place", "INN", "OGRN")
    empty_value_display = "-пусто-"


class Tek_ObjectAdmin(admin.ModelAdmin):
    list_display = ("name", "place", "ul", "category", "region")
    list_filter = ("category", "region")
    empty_value_display = "-пусто-"


admin.site.register(Check, CheckAdmin)
admin.site.register(Category)
admin.site.register(Ul, UlAdmin)
admin.site.register(Tek_Object, Tek_ObjectAdmin)
admin.site.register(Form)
