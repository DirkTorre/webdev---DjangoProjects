from rest_framework import serializers
from core.models import Book


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name")
    genre = serializers.CharField(source="get_genre_display")

    class Meta:
        model = Book
        fields = ("name", "author_name", "price", "genre")
