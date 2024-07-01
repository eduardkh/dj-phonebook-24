# dj-phonebook-24

> first steps environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> first steps django

```powershell
django-admin startproject phonebook .
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

take a look at [Django app on localhost](http://127.0.0.1:8000/)

> create an app

```powershell
python manage.py startapp phonebook_app
```

> add models and migrate

```powershell
python manage.py makemigrations
python manage.py migrate
```
