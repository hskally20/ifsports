from django.db import models

# Modelo de Time
class Time(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    frase_efeito = models.CharField(max_length=100, verbose_name='Frase de Efeito')
    qtd_jogadores = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

# Modelo de Jogador
class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    posicao = models.CharField(max_length=50)  # Exemplo: Goleiro, Atacante
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="jogadores")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.posicao})"

# Modelo de Árbitro
class Arbitro(models.Model):
    nome = models.CharField(max_length=100)
    experiencia = models.PositiveIntegerField(help_text="Anos de experiência")
    cidade = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.cidade}"

# Modelo de Evento
class Evento(models.Model):
    nome = models.CharField(max_length=150)
    data = models.DateField()
    esporte = models.CharField(max_length=50)
    times = models.ManyToManyField(Time, related_name="eventos")
    descricao = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.esporte})"
