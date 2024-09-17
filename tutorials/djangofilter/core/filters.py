import django_filters
from core.models import Book
from django import forms


class BookFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    genre = django_filters.MultipleChoiceFilter(
        choices=Book.GenreChoices.choices, widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Book
        fields = {
            "name": ["istartswith"],
            "author__name": ["icontains"],
            "genre": ["exact"],
        }
