from django.urls import path
from . import views

app_name = 'temperature_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('predict_temperature/', views.predict_temperature, name='predict_temperature'),
]