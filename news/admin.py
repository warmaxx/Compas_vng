from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date_create", "date_start", "date_end", )
    search_fields = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(News,NewsAdmin)
