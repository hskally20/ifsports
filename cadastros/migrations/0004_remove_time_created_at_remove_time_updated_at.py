# Generated by Django 5.1.3 on 2024-11-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_alter_time_options_alter_time_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='time',
            name='updated_at',
        ),
    ]
