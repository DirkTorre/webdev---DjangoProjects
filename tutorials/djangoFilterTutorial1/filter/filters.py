import django_filters

from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = []

class BookFilter2(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    year = django_filters.NumberFilter()
    year__gt = django_filters.NumberFilter(lookup_expr='year__gt')
    year__lt = django_filters.NumberFilter(lookup_expr='year__lt')

    class Meta:
        model = Book
        fields = ['author']