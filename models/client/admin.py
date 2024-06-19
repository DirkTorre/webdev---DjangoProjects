from django.contrib import admin

from .models import Client, TodoList, Comment

admin.site.register(Client)
admin.site.register(TodoList)
admin.site.register(Comment)

