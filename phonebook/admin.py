from django.contrib import admin

# Register your models here.
from .models import Contact, Rank, Job, Departament

admin.site.register(Contact)
admin.site.register(Rank)
admin.site.register(Job)
admin.site.register(Departament)
