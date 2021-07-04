"""Gastroler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from homepage import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'homepage'
urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('vng_stat/', include('vng_stat.urls'), name='vng_stat'),
    path('vng_incidents/', include('vng_incidents.urls'), name='vng_incidents'),
    path('phonebook/', include('phonebook.urls'), name='phonebook'),
    path('report_result/', include('report_result.urls'), name='report_result'),
    #Admin pages
    path('admin/', admin.site.urls, name='admin'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)