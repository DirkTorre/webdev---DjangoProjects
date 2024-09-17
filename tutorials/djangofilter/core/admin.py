from django.contrib import admin
from .models import Book, Author


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "number_in_stock", "genre", "author")
    list_filter = ("name", "price", "number_in_stock", "genre", "author")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
