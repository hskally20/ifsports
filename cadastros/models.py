from django.db import models

# Modelo de Time
class Time(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    frase_efeito = models.CharField(max_length=100 ,name='frase de efeito')
    qtd_jogadores = models.IntegerField()

    def __str__(self):
        return self.nome

# Modelo de Jogador
class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    posicao = models.CharField(max_length=50)  # Exemplo: Goleiro, Atacante
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="jogadores")

    def __str__(self):
        return f"{self.nome} ({self.posicao})"

# Modelo de Árbitro
class Arbitro(models.Model):
    nome = models.CharField(max_length=100)
    experiencia = models.PositiveIntegerField(help_text="Anos de experiência")
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.cidade}"
