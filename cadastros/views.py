from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Time, Jogador, Arbitro, Evento

# Views para Time
class TimeListView(ListView):
    model = Time
    template_name = 'listar/times.html'
    context_object_name = 'times'

class TimeCreateView(CreateView):
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar/times')

class TimeUpdateView(UpdateView):
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar/times')

class TimeDeleteView(DeleteView):
    model = Time
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-times')

# Views para Jogador
class JogadorListView(ListView):
    model = Jogador
    template_name = 'jogador/listar-jogadores.html'
    context_object_name = 'jogadores'

class JogadorCreateView(CreateView):
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'time']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-jogadores')

class JogadorUpdateView(UpdateView):
    model = Jogador
    fields = ['nome', 'idade', 'posicao', 'time']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-jogadores')

class JogadorDeleteView(DeleteView):
    model = Jogador
    template_name = '.html'
    success_url = reverse_lazy('listar-jogadores')

# Views para Árbitro
class ArbitroListView(ListView):
    model = Arbitro
    template_name = 'arbitro/listar_arbitros.html'
    context_object_name = 'arbitros'

class ArbitroCreateView(CreateView):
    model = Arbitro
    fields = ['nome', 'experiencia', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-arbitros')

class ArbitroUpdateView(UpdateView):
    model = Arbitro
    fields = ['nome', 'experiencia', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-arbitros')

class ArbitroDeleteView(DeleteView):
    model = Arbitro
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-arbitros')

# Views para Evento
class EventoListView(ListView):
    model = Evento
    template_name = 'evento/listar-eventos.html'
    context_object_name = 'eventos'

class EventoCreateView(CreateView):
    model = Evento
    fields = ['nome', 'data', 'esporte', 'times', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-eventos')

class EventoUpdateView(UpdateView):
    model = Evento
    fields = ['nome', 'data', 'esporte', 'times', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-eventos')

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-eventos')
