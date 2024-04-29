from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgendamentoForm
from .models import Agendamento
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout

def agendar_consulta(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            if agendamento.data_horario > timezone.now():
                agendamento.save()
                return redirect('agendamento_sucesso')
            else:
                form.add_error('data_horario', 'Não é possível agendar para uma data/hora passada.')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento_app/agendar_consulta.html', {'form': form})


def agendamento_sucesso(request):
    return render(request, 'agendamento_app/agendamento_sucesso.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def admin_check(user):
    return user.is_superuser


@login_required
@user_passes_test(admin_check)
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamento_app/index.html', {'agendamentos': agendamentos})


@login_required
@user_passes_test(admin_check)
def editar_agendamentos(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            # Atribuir manualmente os valores não modificáveis para garantir que não sejam perdidos
            form.instance.nome_completo = agendamento.nome_completo
            form.instance.telefone = agendamento.telefone
            form.instance.cpf = agendamento.cpf
            form.save()
            return redirect('listar_agendamentos')
        else:
            print(form.errors)  # Debugar erros de formulário
    else:
        form = AgendamentoForm(instance=agendamento)

    min_date = timezone.now().strftime('%Y-%m-%dT%H:%M')  # Data mínima
    return render(request, 'agendamento_app/editar_agendamento.html', {
        'form': form, 'agendamento': agendamento, 'min_date': min_date
    })


@login_required
@user_passes_test(admin_check)
def remover_agendamento(request, id):
    agendamento = Agendamento.objects.get(id=id)
    agendamento.delete()
    return redirect('listar_agendamentos')