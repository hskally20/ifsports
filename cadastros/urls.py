from django.urls import path
from .views import (
    TimeListView, TimeCreateView, TimeUpdateView, TimeDeleteView,
    JogadorListView, JogadorCreateView, JogadorUpdateView, JogadorDeleteView,
    ArbitroListView, ArbitroCreateView, ArbitroUpdateView, ArbitroDeleteView,
    EventoListView, EventoCreateView, EventoUpdateView, EventoDeleteView
)

urlpatterns = [
    # Rotas para Times
    path('times/', TimeListView.as_view(), name='listar_times'),
    path('times/criar/', TimeCreateView.as_view(), name='criar_time'),
    path('times/editar/<int:pk>/', TimeUpdateView.as_view(), name='editar_time'),
    path('times/excluir/<int:pk>/', TimeDeleteView.as_view(), name='excluir_time'),

    # Rotas para Jogadores
    path('jogadores/', JogadorListView.as_view(), name='listar_jogadores'),
    path('jogadores/criar/', JogadorCreateView.as_view(), name='criar_jogador'),
    path('jogadores/editar/<int:pk>/', JogadorUpdateView.as_view(), name='editar_jogador'),
    path('jogadores/excluir/<int:pk>/', JogadorDeleteView.as_view(), name='excluir_jogador'),

    # Rotas para Árbitros
    path('arbitros/', ArbitroListView.as_view(), name='listar_arbitros'),
    path('arbitros/criar/', ArbitroCreateView.as_view(), name='criar_arbitro'),
    path('arbitros/editar/<int:pk>/', ArbitroUpdateView.as_view(), name='editar_arbitro'),
    path('arbitros/excluir/<int:pk>/', ArbitroDeleteView.as_view(), name='excluir_arbitro'),

    # Rotas para Eventos
    path('eventos/', EventoListView.as_view(), name='listar_eventos'),
    path('eventos/criar/', EventoCreateView.as_view(), name='criar_evento'),
    path('eventos/editar/<int:pk>/', EventoUpdateView.as_view(), name='editar_evento'),
    path('eventos/excluir/<int:pk>/', EventoDeleteView.as_view(), name='excluir_evento'),
]
