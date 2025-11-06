from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name="author_name")
books_by_author = Book.objects.filter(author=author)

library = Library.objects.get(name="library_name")
books_in_library = library.books.all()

librarian = Librarian.objects.get(library=library)
