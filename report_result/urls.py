from django.urls import path
from report_result import views

app_name = 'report_result'
urlpatterns = [
    path('', views.index, name='index'),
    path('week/', views.week, name ='week')
]
