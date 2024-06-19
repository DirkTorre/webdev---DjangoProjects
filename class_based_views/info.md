# Superuser details:
- username: dirk
- password: wachtwoord


# django protocol
1. start project
2. create the database
3. create superuser
4. start app
    1. register app in INSTALLED_APPS (settings.py of the project app)
    2. create a view for app
    3. create urls.py for the app
    4. register app urls.py in project urls.py

optional

1. create model for app
2. stage migrations for app model
3. migrate changes
4. register model in admin.py for the app
5. use model in view 


# commands
```bash
# starting a new django project
django-admin startproject <project name> <name of project folder>/

# starting a new django project using a template (you can also use url)
django-admin startproject <project name> <naam van hoofd map>/ --template <location of other project to use as template>

# running the server
python manage.py runserver

# creating database or applying changes
python manage.py migrate

# create database superuser
python manage.py createsuperuser

# starting an app in the project
python manage.py startapp <app name>

# staging changes per model
python manage.py makemigrations <model name>
```

# notes
redirect: naar een ander scherm gaan.

Je kan een redirect gebruiken om taken uit te voeren voordat de gebruiker bij de pagina komt.

The pattern_name or template name you define in the redirect class will be loaded after the method is done executing.

pattern_name = 'cbv:singlepost'
template_name = "ex4.html"





