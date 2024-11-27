from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Time, Jogador, Arbitro, Evento
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'usuarios/profile.html')

# Mixins de grupo
class GroupRequiredMixin(LoginRequiredMixin):
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if self.group_required:
            group = Group.objects.get(name=self.group_required)
            if not request.user.groups.filter(name=group.name).exists():
                return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        return super().dispatch(request, *args, **kwargs)

# Views para Time
class TimeList(GroupRequiredMixin, ListView):
    model = Time
    template_name = 'listas/time.html'
    context_object_name = 'times'
    paginate_by = 5
    def get_queryset(self):
        queryset = Time.objects.all()
        time_busca = self.request.GET.get('time')

        if time_busca:
            queryset = queryset.filter(Q(nome__icontains=time_busca) | Q(frase_efeito__icontains=time_busca))

        return queryset


class TimeCreateView(GroupRequiredMixin, CreateView):
    
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-times')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Criar Time'
        return context

class TimeUpdate(GroupRequiredMixin, UpdateView):
   
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-times')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Atualizar Time'
        return context

class TimeDelete(GroupRequiredMixin, DeleteView):
    
    model = Time
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-times')
# Views para Jogador
class JogadorList(GroupRequiredMixin, ListView):
    model = Jogador
    template_name = 'listas/jogadores.html'  # Alterado
    context_object_name = 'jogadores'
    group_required = 'Admin'


class JogadorCreateView(GroupRequiredMixin, CreateView):
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'time']
    template_name = 'listas/form.html'  # Alterado
    success_url = reverse_lazy('listar_jogadores')  # Alterado
    group_required = 'Admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Criar Jogador'
        return context


class JogadorUpdate(GroupRequiredMixin, UpdateView):
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'time']
    template_name = 'listas/form.html'  # Alterado
    success_url = reverse_lazy('listar_jogadores')  # Alterado
    group_required = 'Admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Atualizar Jogador'
        return context


class JogadorDelete(GroupRequiredMixin, DeleteView):
    model = Jogador
    template_name = 'listas/form-excluir.html'  # Alterado
    success_url = reverse_lazy('listar_jogadores')  # Alterado
    group_required = 'Admin'


# Views para Árbitro
class ArbitroList(GroupRequiredMixin, ListView):
    model = Arbitro
    template_name = 'listas/arbitros.html'  # Alterado
    context_object_name = 'arbitros'
    group_required = 'Admin'


class ArbitroCreateView(GroupRequiredMixin, CreateView):
    model = Arbitro
    fields = ['nome', 'experiencia', 'cidade']
    template_name = 'listas/form.html'  # Alterado
    success_url = reverse_lazy('listar_arbitros')  # Alterado
    group_required = 'Admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Criar Árbitro'
        return context


class ArbitroUpdate(GroupRequiredMixin, UpdateView):
    model = Arbitro
    fields = ['nome', 'experiencia', 'cidade']
    template_name = 'listas/form.html'  # Alterado
    success_url = reverse_lazy('listar_arbitros')  # Alterado
    group_required = 'Admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Atualizar Árbitro'
        return context


class ArbitroDelete(GroupRequiredMixin, DeleteView):
    model = Arbitro
    template_name = 'listas/form-excluir.html'  # Alterado
    success_url = reverse_lazy('listar_arbitros')  # Alterado
    group_required = 'Admin'


# Views para Evento
class EventoList(GroupRequiredMixin, ListView):
    model = Evento
    template_name = 'listas/eventos.html'  # Alterado
    context_object_name = 'eventos'
    group_required = 'Admin'


class EventoCreateView(GroupRequiredMixin, CreateView):
    model = Evento
    fields = ['nome', 'data', 'esporte', 'times', 'descricao']
    template_name = 'listas/form.html' 
    success_url = reverse_lazy('listar_eventos')  
    group_required = 'Admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Criar Evento'
        return context


class EventoUpdate(GroupRequiredMixin, UpdateView):
    model = Evento
    fields = ['nome', 'data', 'esporte', 'times', 'descricao']
    template_name = 'listas/form.html'  
    success_url = reverse_lazy('listar_eventos')  
    group_required = 'Admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Atualizar Evento'
        return context


class EventoDelete(GroupRequiredMixin, DeleteView):
    model = Evento
    template_name = 'listas/form-excluir.html'  
    success_url = reverse_lazy('listar_eventos')  
    group_required = 'Admin'