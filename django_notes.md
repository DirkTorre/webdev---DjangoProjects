# django protocol
1. start project
2. create the database
3. create superuser
4. start app
    1. register app in INSTALLED_APPS (settings.py of the project app)
    2. create a view for app
    3. create urls.py for the app
    4. register app_name in app urls.py
    5. register app urls.py in project urls.py

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


# models
Every database model made will automatically have an primary key called id of type bigint.
in the django admin you can deselect linked objects with ctrl+click.

## fields
### slugfield
A slugfield is a url friendly version of charfield.

- slug input: Hello World.
- slug data: hello-world.

### imagefield
models.ImageField(upload_to='media/articles')

### charfield
- blank = True: gives a option to include "".
- null=True: allows null values in database.

The problem you will get is that there will be 2 types of no value in the database.

### PositiveSmallIntegerField


## meta info
Every model van have a Meta class, can be used for ordering and stuff.
### ordering
Reverse ordering can be done with a - symbol.
```python
class Meta:
        ordering = ['-name']
```
### verbose_name
changes how the class/table is displayed in django admin.
### abstract
Does not include the model in the django-admin.
handy for mixins and the variable version of mixins.

## functions
Allows you to execute code before object is saved.
Very handy.
```python
def save(self, *args, **kwargs):
        print("Saved")
        super(Client, self).save(*args, **kwargs)
```

## constraints
BaseConstraint()
CheckConstraint()
UniqueConstraint()

## validators

## fixtures
Fixtures are a way to populate a database with dummie data.
The data is in JSON format.
the json can be stores in a 'fixtures' directory in your app.
then run 
```bash
python manage.py loaddata school
```


# django admin
You can add custom columns and filters and more!
https://realpython.com/customize-django-admin-python/

You can create different admin sites.
So it's possible to create different admin experiences for different roles.

In the admin file, you can put methods to create extra info that's not in the database. like calculating the average.
You can always change the titles of columns. You can also add html!
you can add links to subsets of tables!
You can add filters to the list screen!
you can also change the order of the forms.
Field names can also be changed (does not affect database).
je kan ook een modelform gebruiken in je admin pagina.
