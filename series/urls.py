from django.urls import path
from . import views

urlpatterns = [
    path ('evaluacion2', views.lista_series, name='lista_series'),
]
