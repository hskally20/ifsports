from django.urls import path
from .views import IndexView
from django.contrib.auth import views as auth_views


urlpatterns = [
    #cadastros 
    path('', IndexView.as_view(), name='inicio'),
    ]