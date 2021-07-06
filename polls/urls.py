from django.urls import path
from . import views
from django.conf import settings

app_name = 'polls'

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),
    path('impressum/', views.impressum, name='impressum'),
    path('test/', views.test, name='test'),
]  


