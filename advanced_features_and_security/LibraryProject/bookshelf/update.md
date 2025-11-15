from bookshelf.models import Book

#retrieving the book with the title "1984"
>>> book = Book.objects.get(title = "1984")

#updating the title of the book
>>> book.title = "Nineteen Eighty-Four"

#save the update
>>> book.save()

verifying update
#retrieving updated book
updated_book = Book.objects.get(author="George Orwell")

#printing the updated title
print(f"Updated title: {updated_book.title}")

#output
Updated title: Nineteen Eighty-Four