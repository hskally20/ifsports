from django.db import models

# Modelo de Time
class Time(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    frase_efeito = models.CharField(max_length=100, verbose_name='Frase de Efeito')
    qtd_jogadores = models.IntegerField()

    def __str__(self):
        return self.nome


# Modelo de Jogador
class Jogador(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Jogador")
    idade = models.PositiveIntegerField(verbose_name="Idade")
    posicao = models.CharField(max_length=50, verbose_name="Posição")  # Exemplo: Goleiro, Atacante
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="jogadores", verbose_name="Time")

    def __str__(self):
        return f"{self.nome} ({self.posicao})"


# Modelo de Árbitro
class Arbitro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Árbitro")
    experiencia = models.PositiveIntegerField(help_text="Anos de experiência", verbose_name="Experiência")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")

    def __str__(self):
        return f"{self.nome} - {self.cidade}"


# Modelo de Evento
class Evento(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do Evento")
    data = models.DateField(verbose_name="Data do Evento")
    esporte = models.CharField(max_length=50, verbose_name="Esporte")
    times = models.ManyToManyField(Time, related_name="eventos", verbose_name="Times Participantes")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return f"{self.nome} ({self.esporte})"
