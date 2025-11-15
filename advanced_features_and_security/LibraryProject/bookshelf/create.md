from bookshelf.models import Book

#creating the book instance
>>> book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)

#calling the book instance
>>> book

#output
<Book: 1984 by George Orwell (1949)>
