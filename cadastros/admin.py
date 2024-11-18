from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Time, Jogador, Arbitro

admin.site.register(Time)
admin.site.register(Jogador)
admin.site.register(Arbitro)