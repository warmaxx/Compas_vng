from django.urls import path, include
from . import views

app_name = 'vng_info'
urlpatterns = [
    path('', views.index, name='index'),
    path('pers/', views.pers, name='pers'),
]
