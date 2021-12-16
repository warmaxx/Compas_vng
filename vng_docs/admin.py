from django.contrib import admin

# Register your models here.
from .models import Folder, File


class FileAdmin(admin.ModelAdmin):
    list_display = ("name", "folder",)
    search_fields = ("name",)
    list_filter = ("folder",)
    empty_value_display = "-пусто-"


admin.site.register(Folder)
admin.site.register(File, FileAdmin)
