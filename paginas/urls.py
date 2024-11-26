from django.urls import path
from .views import IndexView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # login 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view (),  name='logout'),

    #cadastros 
    path('', IndexView.as_view(), name='inicio'),
    ]