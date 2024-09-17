from django.core.management.base import BaseCommand
from core.models import Book, Author


class Command(BaseCommand):
    help = "load book data"

    def handle(self, *args, **kwargs):
        # create authors
        orwell = Author.objects.get_or_create(name="George Orwell")[0]
        hawking = Author.objects.get_or_create(name="Stephen Hawkin")[0]
        adams = Author.objects.get_or_create(name="Douglas Adams")[0]

        Book.objects.get_or_create(
            name="1984",
            author=orwell,
            price=10.99,
            genre=Book.GenreChoices.SCI_FI,
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
            name="The Hitchhiker's Guide to the Galaxy",
            author=adams,
            price=4.69,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=10,
        )
