from django.urls import path
from vng_incidents import views

app_name = 'vng_incidents'
urlpatterns = [
    path('', views.index, name='index'),
    path('incs/', views.incs, name='incs')
]
