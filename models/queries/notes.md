## admin
user:       dirk
password:   wachtwoord

## websites

[Django 4.1: Making queries](https://docs.djangoproject.com/en/4.1/topics/db/queries/)

[queryset api reference](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#queryset-api)

## models

### create a object

```python
from djangoproject.models import Blog, Entry
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()

e = Entry(blog=b, pub_date="1910-10-20")
e.save()
```

### saving a foreign key

```python
# get all values of a object
Blog.objects.all()[0].__dict__

# linking object as foreign key
entry = Entry.objects.get(pk=1)
entry.blog = Blog.objects.get(name='new name')
entry.save()
```

### updating a many to many field

```python
from djangoproject.models import Author
joe = Author.objects.create(name="Joe")
entry.authors.add(joe)
```

add multiple records to a many to many field

```python
john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")
entry.authors.add(john, paul, george, ringo)
```

### queries

qieries resultes can be saved, so the query does ot have to be executed every time you need it. just save the resukt as a variable.

look at: https://docs.djangoproject.com/en/4.1/ref/models/querysets/#queryset-api

```python
.objects.all()

Entry.objects.create(headline="aa", pub_date='1910-1-1', blog_id=Blog.objects.get(name='new name').id)
Entry.objects.create(headline="bb", pub_date='1910-1-1', blog_id=Blog.objects.get(name='new name').id)
Entry.objects.create(headline="ba", pub_date='1911-1-1', blog_id=Blog.objects.get(name='new name').id)
Entry.objects.create(headline="ba", pub_date='2025-1-1', blog_id=Blog.objects.get(name='new name').id)


Entry.objects.filter(pub_date__year=1910)

you can chain filters

import datetime
Entry.objects.filter(
    headline__startswith='b'
).exclude(
    pub_date__gte=datetime.date(1910,2,1)
)
```

a queryset only gets executed when it is called.

Entry.objects.order_by('headline')

### Field lookups
Entry.objects.filter(pub_date__lte='1880-1-1')

### Lookups that span relationships
Kan ik gebruiken voor opdracht

hiermee kan je entry object zoeken in blog

```python 
Blog.objects.filter(
...     entry__headline__contains='Lennon',
... ).filter(
...     entry__pub_date__year=2008,
... )
```