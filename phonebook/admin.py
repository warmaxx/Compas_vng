from django.contrib import admin

# Register your models here.
from .models import Contact, Rank, Job, Departament


class ContactAdmin(admin.ModelAdmin):
    list_display = ("sur_name", "name", "patronymic", "departament", "job", "rank", "work_phone", "cell_phone", "email", "status")
    search_fields = ("sur_name","name",)
    list_filter = ("job", "rank", "status")
    empty_value_display = "-пусто-"


class DepartamentAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "address", "type", "position", "count_employees", )
    search_fields = ("name",)
    list_filter = ("type",)
    empty_value_display = "-пусто-"


admin.site.register(Contact, ContactAdmin)
admin.site.register(Rank)
admin.site.register(Job)
admin.site.register(Departament, DepartamentAdmin)
