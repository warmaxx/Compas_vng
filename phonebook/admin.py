from django.contrib import admin

# Register your models here.
from .models import Contact, Rank, Job, Status, Departament

admin.site.register(Contact)
admin.site.register(Rank)
admin.site.register(Job)
admin.site.register(Status)
admin.site.register(Departament)
