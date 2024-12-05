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
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2
        if len(password2) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if password2.isdigit():
            raise forms.ValidationError("A senha não pode ser apenas numérica.")
        # Aqui você pode adicionar mais validações customizadas
        return password2
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

def registrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Formulário válido!")  # Log para debug
            form.save()
            return redirect('login')
        else:
            print("Erros no formulário:", form.errors)  # Log para debug
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrar.html', {'form': form})

# Função de Logout
def logout_view(request):
    logout(request)
    return redirect('inicio')  # Redireciona para a página de login após o logout

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
