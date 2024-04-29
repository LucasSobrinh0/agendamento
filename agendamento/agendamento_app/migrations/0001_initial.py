# Generated by Django 5.0.4 on 2024-04-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=14)),
                ('data_horario', models.DateTimeField()),
            ],
        ),
    ]
