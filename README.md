# Advanced Database Systems Assessment Task

## Installation guideline

Install python and PostgreSQL database

https://www.python.org/downloads/

https://www.postgresql.org/download/

Setup Virtual Environments

```bash
python3 -m venv env
env\Scripts\activate.bat
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

Setup PostgreSQL database config from .env

```bash
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
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
