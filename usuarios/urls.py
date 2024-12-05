from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import UsuarioCreate
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
]
