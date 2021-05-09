from django.urls import path, include
from . import views

app_name = 'vng_stat'
urlpatterns = [
    path('', views.index, name='index'),
    path('stat/', views.stat, name='stat'),
    path('upload/', views.upload, name='upload')
]
