from django.urls import path
from .views import *

urlpatterns = [
    path('', acceder_a_mercadolibre, name='index'),  # Accede a la página de inicio
]

