from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'date_of_publication', 'isbn',
                  'number_of_pages', 'language', 'image_link']
