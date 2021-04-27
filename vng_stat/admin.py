from django.contrib import admin

# Register your models here.
from .models import Check, Category, Ul, Tek_Object, Form

admin.site.register(Check)
admin.site.register(Category)
admin.site.register(Ul)
admin.site.register(Tek_Object)
admin.site.register(Form)