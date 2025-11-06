from bookshelf.models import Book

#retrieving the book with title "Nimeteen Eighty-Four"
>>> book = Book.objects.get(title="Nineteen Eighty-Four")

#delete the book
>>> book.delete()

#output
(1, {'bookshelf.Book': 1})