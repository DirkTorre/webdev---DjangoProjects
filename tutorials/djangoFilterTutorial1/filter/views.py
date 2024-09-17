from django.shortcuts import render
import django_filters

from .models import Book
from .filters import BookFilter

def book_list(request):
    queryset = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=queryset)
    return render(request, 'filter/book_list.html', {'filter': book_filter})