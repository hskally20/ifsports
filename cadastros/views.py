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
    group_required = 'Admin'
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-times')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Criar Time'
        return context

class TimeUpdate(GroupRequiredMixin, UpdateView):
    group_required = 'Admin'
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-times')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Atualizar Time'
        return context

class TimeDelete(GroupRequiredMixin, DeleteView):
    group_required = 'Admin'
    model = Time
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-times')

# Views para Jogador
class JogadorList(GroupRequiredMixin, ListView):
    group_required = 'Admin'
    model = Jogador
    template_name = 'listar/jogadores.html'
    context_object_name = 'jogadores'

class JogadorCreateView(GroupRequiredMixin, CreateView):
    group_required = 'Admin'
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'time']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_jogadores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Criar Jogador'
        return context

class JogadorUpdate(GroupRequiredMixin, UpdateView):
    group_required = 'Admin'
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'time']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_jogadores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Atualizar Jogador'
        return context

class JogadorDelete(GroupRequiredMixin, DeleteView):
    group_required = 'Admin'
    model = Jogador
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar_jogadores')

# Views para Árbitro
class ArbitroList(GroupRequiredMixin, ListView):
    group_required = 'Admin'
    model = Arbitro
    template_name = 'arbitro/listar_arbitros.html'
    context_object_name = 'arbitros'

class ArbitroCreateView(GroupRequiredMixin, CreateView):
    group_required = 'Admin'
    model = Arbitro
    fields = ['nome', 'experiencia', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_arbitros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Criar Árbitro'
        return context

class ArbitroUpdate(GroupRequiredMixin, UpdateView):
    group_required = 'Admin'
    model = Arbitro
    fields = ['nome', 'experiencia', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_arbitros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Atualizar Árbitro'
        return context

class ArbitroDelete(GroupRequiredMixin, DeleteView):
    group_required = 'Admin'
    model = Arbitro
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar_arbitros')

# Views para Evento
class EventoList(GroupRequiredMixin, ListView):
    group_required = 'Admin'
    model = Evento
    template_name = 'evento/listar-eventos.html'
    context_object_name = 'eventos'

class EventoCreateView(GroupRequiredMixin, CreateView):
    group_required = 'Admin'
    model = Evento
    fields = ['nome', 'data', 'esporte', 'times', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_eventos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Criar Evento'
        return context

class EventoUpdate(GroupRequiredMixin, UpdateView):
    group_required = 'Admin'
    model = Evento
    fields = ['nome', 'data', 'esporte', 'times', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_eventos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Atualizar Evento'
        return context

class EventoDelete(GroupRequiredMixin, DeleteView):
    group_required = 'Admin'
    model = Evento
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar_eventos')
