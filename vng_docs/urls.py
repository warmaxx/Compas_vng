from django.urls import path, include
from . import views

app_name = 'vng_docs'
urlpatterns = [
    path('', views.index, name='index'),
    path('folder/<int:folder_id>/', views.folder, name='folder'),
]
