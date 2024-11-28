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


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        return confirm_password



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

# Página de Perfil (necessário estar logado para acessar)
@login_required
def profile_view(request):
    return render(request, 'usuarios/profile.html')


# Registro de novo usuário (usando CreateView)

class UsuarioCreate(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registrar-se.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.success_url)

