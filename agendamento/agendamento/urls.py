from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agendamento_app.urls')),
    # Garante que quando o usuário acessar o site, irá ser redirecionado para a url correta!
]
