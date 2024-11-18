from django.urls import path
from .views import TimeCreate, 
from .views import TimeUpdate,
from .views import TimeList,
from .views import TimeDelete,

urlpatterns = [
    # Rotas para Times
   
    path('times/', views.listar_times, name='listar_times'),
    path('times/criar/', views.criar_time, name='criar_time'),
    path('times/editar/<int:id>/', views.editar_time, name='editar_time'),
    path('times/deletar/<int:id>/', views.deletar_time, name='deletar_time'),

    # Adicione rotas para Jogadores e Árbitros aqui (seguindo o mesmo padrão).
]
