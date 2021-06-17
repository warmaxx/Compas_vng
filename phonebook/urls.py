from django.urls import path
from . import views

app_name = 'phonebook'
urlpatterns = [
    path('', views.index, name='index'),
    path('deps/', views.deps, name='deps'),
    path('pers/', views.pers, name='pers'),
    path('change_status/<int:pers_id>/<int:status_id>/', views.change_status, name='change_status'),
    path('change_comment/<int:pers_id>/', views.change_comment, name='change_comment')
]
