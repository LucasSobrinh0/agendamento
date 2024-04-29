Crie um ambiente virtual:
python -m venv env

Instale as dependências:
pip install -r requirements.txt

Entre no diretório de agendamentos:
cd agendamentos

migre as os dados:
python manage.py makemigrations
python manage.py migrate

Crie um super usuário para utilziar o sistema:
python manage.py createsuperuser

Agora rode o servidor:
python manage.py runserver
