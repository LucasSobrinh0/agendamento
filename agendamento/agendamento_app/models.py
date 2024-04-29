from django.db import models

# Modelo para guardar informações de agendamentos
class Agendamento(models.Model):
    nome_completo = models.CharField(max_length=255)  # Campo para o nome completo do usuário
    telefone = models.CharField(max_length=20)        # Campo para o telefone do usuário
    cpf = models.CharField(max_length=14)             # Campo para o CPF do usuário
    data_horario = models.DateTimeField()             # Campo para a data e hora do agendamento

    def __str__(self):
        # Método que define a representação em string do objeto, útil para exibição no admin
        return f"{self.nome_completo} - {self.data_horario.strftime('%d/%m/%Y %H:%M')}"
