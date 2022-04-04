# Advanced Database Systems Assessment Task

## Installation guideline

Install python and PostgreSQL database

https://www.python.org/downloads/

https://www.postgresql.org/download/

Setup Virtual Environments

```bash
python3 -m venv django_env
django_env\Scripts\activate.bat
```

Clone this repository

```bash
git clone https://github.com/MohsinUddinAbir/django_crud_app.git
```

Enter on project root and install dependency

```bash
cd django_crud_app
pip install -r requirements.txt
```

Setup PostgreSQL database name, username and password from /core/settings.py

```py
DATABASES = {
    'default': {
         #...
        'NAME': 'blogapp',
        'USER': 'postgres',
        'PASSWORD': '1234',
         #...
    }
}
```

Migrate database

```bash
python manage.py makemigrations
python manage.py migrate
```

Run project

```bash
python manage.py runserver
```
