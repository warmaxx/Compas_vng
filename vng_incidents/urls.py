from django.urls import path
from . import views

app_name = 'vng_incidents'
urlpatterns = [
    path('', views.index, name='index')
]
