# Advanced Database Systems Assessment Task

## Installation guideline

Install python

https://www.python.org/downloads/

Setup Virtual Environments

```bash
python3 -m venv django_env
django_env\Scripts\activate.bat
```

Clone this repository and enter on project root

```bash
git clone https://github.com/MohsinUddinAbir/django_crud_app.git
cd django_crud_app
```

Install dependency

```bash
pip install -r requirements.txt
```

Setup database name, username and password from /core/settings.py

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
python manage.py migrate
```

Run project

```bash
python manage.py runserver
```
