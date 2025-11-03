from django.urls import path
from Prediccion import views

urlpatterns = [
    path('', views.index, name='home'),
    path('predecir/', views.predecir, name='predecir'),
]