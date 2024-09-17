from django.core.management.base import BaseCommand
from core.models import Book, Author


class Command(BaseCommand):
    help = "load book data"

    def handle(self, *args, **kwargs):
        # create authors
        orwell = Author.objects.get_or_create(name="George Orwell")[0]
        hawking = Author.objects.get_or_create(name="Stephen Hawkin")[0]
        adams = Author.objects.get_or_create(name="Douglas Adams")[0]
        doyle = Author.objects.get_or_create(name=" Arthur Conan Doyle")[0]

        Book.objects.get_or_create(
            name="1984",
            author=orwell,
            price=10.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=4,
        )

        Book.objects.get_or_create(
            name="Down and Out in Paris and London",
            author=orwell,
            price=8.66,
            genre=Book.GenreChoices.OTHER,
            number_in_stock=4,
        )

        Book.objects.get_or_create(
            name="A Brief History of Time",
            author=hawking,
            price=9.99,
            genre=Book.GenreChoices.NON_FICTION,
            number_in_stock=5,
        )

        Book.objects.get_or_create(
            name="Dirk Gently's Holistic Detective Agency",
            author=adams,
            price=5.99,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=10,
        )

        Book.objects.get_or_create(
            name="The Hitchhiker's Guide to the Galaxy",
            author=adams,
            price=6.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=10,
        )

        Book.objects.get_or_create(
            name="A Study in Scarlet",
            author=doyle,
            price=5.99,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=8,
        )

        Book.objects.get_or_create(
            name="The Hound of the Baskervilles",
            author=doyle,
            price=5.89,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=8,
        )
