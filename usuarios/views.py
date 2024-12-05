from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
class UsuarioCreate(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registrar.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)  # Faz o login automaticamente após o registro
        return redirect(self.success_url)

# Função de Logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirecione para a página inicial ou desejada
        else:
            messages.error(request, "Usuário ou senha inválidos. Tente novamente.")
    return render(request, 'login.html')
