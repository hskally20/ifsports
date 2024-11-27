from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth.models import User


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

# View de Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Autentica o usuário
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redireciona para a página de perfil após o login
            else:
                # Caso o usuário não seja autenticado
                form.add_error(None, 'Usuário ou senha inválidos')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Página de Perfil (necessário estar logado para acessar)
@login_required
def profile_view(request):
    return render(request, 'usuarios/profile.html')


# Registro de novo usuário (usando CreateView)
class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = 'usuarios/form.html'
    success_url = reverse_lazy('login')  # Redireciona para a página de login após o registro

    def form_valid(self, form):
        # Verifica se o grupo 'Paciente' existe
        grupo = get_object_or_404(Group, name='Paciente')
        # Chama o método form_valid da superclasse para salvar o formulário
        response = super().form_valid(form)
        # Adiciona o usuário ao grupo
        self.object.groups.add(grupo)
        self.object.save()
        return response

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = 'Registrar Novo Usuário'
        return context

