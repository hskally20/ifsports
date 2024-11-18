# Generated by Django 5.1.3 on 2024-11-18 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('experiencia', models.PositiveIntegerField(help_text='Anos de experiência')),
                ('cidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('frase de efeito', models.CharField(max_length=100)),
                ('qtd_jogadores', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.PositiveIntegerField()),
                ('posicao', models.CharField(max_length=50)),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogadores', to='cadastros.time')),
            ],
        ),
    ]