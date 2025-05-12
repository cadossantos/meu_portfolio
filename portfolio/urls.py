from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.lista_projetos, name='projetos'),
    path('detalhes/<str:id_projeto>/', views.detalhes_projeto, name='detalhes_projeto')
]