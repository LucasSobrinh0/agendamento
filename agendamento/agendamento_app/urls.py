from django.urls import path, include
from .views import agendar_consulta, agendamento_sucesso, listar_agendamentos, editar_agendamentos, remover_agendamento, logout_view

urlpatterns = [
    path('', agendar_consulta, name='agendar_consulta'),
    path('sucesso/', agendamento_sucesso, name='agendamento_sucesso'),
    path('listar/', listar_agendamentos, name='listar_agendamentos'),
    path('editar/<int:id>/', editar_agendamentos, name='editar_agendamentos'),
    path('remover/<int:id>/', remover_agendamento, name='remover_agendamento'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name='logout_view'),
]
