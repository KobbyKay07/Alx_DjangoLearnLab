from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer): 
    """
    BookSerializer converts Book model instances to/from JSON.

    Relationship Handling:
    The 'author' field is represented by its ID by default.
    This serializer is used for:
        * creating books
        * listing books
        * updating books
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']

        def validate_publication_year(self, value):
            current_year = datetime.now().year
            if value.year > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes Author data without including related books.
    Useful for:
     creating authors
     listing authors
    """

    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name']