from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class MovieStatusAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year')
    list_filter = ('title', 'author', 'year')