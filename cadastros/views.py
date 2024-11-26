from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Time, Jogador, Arbitro, Evento

# Views para Time
class TimeList(ListView):
    model = Time
    template_name = 'listar/times.html'
    context_object_name = 'times'

class TimeCreateView(CreateView):
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_times')

class TimeUpdate(UpdateView):
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_times')

class TimeDelete(DeleteView):
    model = Time
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar_times')

# Views para Jogador
class JogadorList(ListView):
    model = Jogador
    template_name = 'listar/jogadores.html'
    context_object_name = 'jogadores'

class JogadorCreateView(CreateView):
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'time']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_jogadores')

class JogadorUpdate(UpdateView):
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'time']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_jogadores')

class JogadorDelete(DeleteView):
    model = Jogador
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar_jogadores')

# Views para Árbitro
class ArbitroList(ListView):
    model = Arbitro
    template_name = 'arbitro/listar_arbitros.html'
    context_object_name = 'arbitros'

class ArbitroCreateView(CreateView):
    model = Arbitro
    fields = ['nome', 'experiencia', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_arbitros')

class ArbitroUpdate(UpdateView):
    model = Arbitro
    fields = ['nome', 'experiencia', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_arbitros')

class ArbitroDelete(DeleteView):
    model = Arbitro
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar_arbitros')

# Views para Evento
class EventoList(ListView):
    model = Evento
    template_name = 'evento/listar-eventos.html'
    context_object_name = 'eventos'

class EventoCreateView(CreateView):
    model = Evento
    fields = ['nome', 'data', 'esporte', 'times', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_eventos')

class EventoUpdate(UpdateView):
    model = Evento
    fields = ['nome', 'data', 'esporte', 'times', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_eventos')

class EventoDelete(DeleteView):
    model = Evento
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar_eventos')
