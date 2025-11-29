from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Author Model represents an author in the system.

    Fields:
     name: The full name of the author.

    Relationship:
     An Author can have many Books (One-to-Many relationship).
      This is implemented through the ForeignKey in the Book model.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book Model represents a book written by an author.

    Fields:
    title: The title of the book.
    publication_year: Year the book was published.
    author: A ForeignKey linking each book to its author.

    Relationship:
    Each Book belongs to exactly one Author.
    An Author can have many Books.
    The ForeignKey establishes this One-to-Many relationship.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.DateField()

    def __str__(self):
        return self.title