from django.urls import path
from . import views

app_name = 'arrhythmia_detection'

urlpatterns = [
    path('', views.arrhythmia_home, name='arrhythmia_home'),
]