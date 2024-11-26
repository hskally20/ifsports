from django.urls import path
from .views import  TimeList, TimeCreateView, TimeUpdate, TimeDelete
from .views import  JogadorList, JogadorCreateView, JogadorUpdate, JogadorDelete
from .views import  ArbitroList, ArbitroCreateView, ArbitroUpdate, ArbitroDelete
from .views import  EventoList, EventoCreateView, EventoUpdate, EventoDelete


urlpatterns = [
    # Rotas para Times
    path('listar_times/', TimeList.as_view(), name='listar_times'),
    path('criar_time/', TimeCreateView.as_view(), name='criar_time'),
    path('editar_time/<int:pk>/', TimeUpdate.as_view(), name='editar_time'),
    path('excluir_time/<int:pk>/', TimeDelete.as_view(), name='excluir_time'),
     # URLs para Jogador
    path('listar_jogadores/', JogadorList.as_view(), name='listar_jogadores'),
    path('criar_jogador/', JogadorCreateView.as_view(), name='criar_jogador'),
    path('editar_jogador/<int:pk>/', JogadorUpdate.as_view(), name='editar_jogador'),
    path('excluir_jogador/<int:pk>/', JogadorDelete.as_view(), name='excluir_jogador'),

    # URLs para Árbitro
    path('listar_arbitros/', ArbitroList.as_view(), name='listar_arbitros'),
    path('criar_arbitro/', ArbitroCreateView.as_view(), name='criar_arbitro'),
    path('editar_arbitro/<int:pk>/', ArbitroUpdate.as_view(), name='editar_arbitro'),
    path('excluir_arbitro/<int:pk>/', ArbitroDelete.as_view(), name='excluir_arbitro'),

    # URLs para Evento
    path('listar_eventos/', EventoList.as_view(), name='listar_eventos'),
    path('criar_evento/', EventoCreateView.as_view(), name='criar_evento'),
    path('editar_evento/<int:pk>/', EventoUpdate.as_view(), name='editar_evento'),
    path('excluir_evento/<int:pk>/', EventoDelete.as_view(), name='excluir_evento'),
]
