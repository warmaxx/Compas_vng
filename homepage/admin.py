from django.contrib import admin

# Register your models here.
from .models import FedRegion, Region

admin.site.register(FedRegion)
admin.site.register(Region)
