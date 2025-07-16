from django.urls import path
from . import views

urlpatterns = [
    path('reserva/', views.reservar_campo, name='reservar_campo'),
    path('cadastro/', views.cadastrar_campo, name='cadastrar_campo'),  # NOVO
]