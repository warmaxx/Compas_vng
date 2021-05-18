from django.urls import path
from . import views

app_name = 'phonebook'
urlpatterns = [
    path('', views.index, name='index')
]
