from bookshelf.models import Book

#retrieving the book with the title "1984"
>>> book = Book.objects.get(title = "1984")

#print the title of the book
>>> print(f"Title: {book.title}")
#output
Title: 1984

#print the author of the book
>>> print(f"Author: {book.author}")
#output
Author: George Orwell

#print the publication year of the book
>>> print(f"Publication Year: {book.publication_year}")
#output
Publication Year: 1949
