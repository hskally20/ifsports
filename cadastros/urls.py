from django.urls import path
from .views import TimeCreateView, TimeUpdateView, TimeDeleteView, TimeListView

urlpatterns = [
    path('inicio', IndexView.as_view(), name='inicio'),
    path('criar/', TimeCreateView.as_view(), name='criar_time'),
    path('editar/<int:pk>/', TimeUpdateView.as_view(), name='editar_time'),
    path('excluir/<int:pk>/', TimeDeleteView.as_view(), name='excluir_time'),
    path('listar/', TimeListView.as_view(), name='listar_times'),
]
   