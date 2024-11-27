from django.urls import path
from .views import  TimeList, TimeCreateView, TimeUpdate, TimeDelete
from .views import  JogadorList, JogadorCreateView, JogadorUpdate, JogadorDelete
from .views import  ArbitroList, ArbitroCreateView, ArbitroUpdate, ArbitroDelete
from .views import  EventoList, EventoCreateView, EventoUpdate, EventoDelete

urlpatterns = [
    # Rotas para Times
    path('cadastrar/time/', TimeCreateView.as_view(), name='cadastrar-time'),
    path('editar/time/<int:pk>/', TimeUpdate.as_view(), name='editar-time'),
    path('excluir/time/<int:pk>/', TimeDelete.as_view(), name='excluir-time'),
    path('listar/times/', TimeList.as_view(), name='listar-times'),

    # URLs para Jogadores
    path('cadastrar/jogador/', JogadorCreateView.as_view(), name='cadastrar-jogador'),
    path('editar/jogador/<int:pk>/', JogadorUpdate.as_view(), name='editar-jogador'),
    path('excluir/jogador/<int:pk>/', JogadorDelete.as_view(), name='excluir-jogador'),
    path('listar/jogadores/', JogadorList.as_view(), name='listar-jogadores'),

    # URLs para Árbitros
    path('cadastrar/arbitro/', ArbitroCreateView.as_view(), name='cadastrar-arbitro'),
    path('editar/arbitro/<int:pk>/', ArbitroUpdate.as_view(), name='editar-arbitro'),
    path('excluir/arbitro/<int:pk>/', ArbitroDelete.as_view(), name='excluir-arbitro'),
    path('listar/arbitros/', ArbitroList.as_view(), name='listar-arbitros'),

    # URLs para Eventos
    path('cadastrar/evento/', EventoCreateView.as_view(), name='cadastrar-evento'),
    path('editar/evento/<int:pk>/', EventoUpdate.as_view(), name='editar-evento'),
    path('excluir/evento/<int:pk>/', EventoDelete.as_view(), name='excluir-evento'),
    path('listar/eventos/', EventoList.as_view(), name='listar-eventos'),
]
