from relationship_app.models import Author, Book, Library, Libraria

author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
print("Books by John Doe:")
for book in books_by_author:
    print(f"- {book.title}")

library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(f"- {book.title} by {book.author.name}")

librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
