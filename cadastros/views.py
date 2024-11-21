from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Time  # Importa apenas o modelo necessário
from django.urls import reverse_lazy


# Criar Time
class TimeCreateView(CreateView):
    model = Time
    fields = ['nome', ' frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_times')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Cadastro de Time'
        return context

# Editar Time
class TimeUpdateView(UpdateView):
    model = Time
    fields = ['nome', 'frase_efeito', 'qtd_jogadores']
    template_name = 'form.html'
    success_url = reverse_lazy('listar_times')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Editar Time'
        return context

# Excluir Time
class TimeDeleteView(DeleteView):
    model = Time
    template_name = 'form-excluir.html'  # Corrigido para incluir extensão .html
    success_url = reverse_lazy('listar_times')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Titulo'] = 'Confirmar Exclusão'
        return context

# Listar Time
class TimeListView(ListView):
    model = Time
    template_name = 'listas/times.html'
    context_object_name = 'times'
    paginate_by = 5

    def get_queryset(self):
        nome = self.request.GET.get('nome')
        if nome:
            times = Time.objects.filter(nome__icontains=nome)
        else:
            times = Time.objects.all()
        return times
