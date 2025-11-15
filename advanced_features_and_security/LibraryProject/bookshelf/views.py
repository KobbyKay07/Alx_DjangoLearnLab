from django.shortcuts import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
def book_shelf(request):
    return HttpResponse("Hello, welcome to the Bookshelf app!")

# View: List all books
# Permission: can_view
# Only users with can_view can access this page.
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    """
    Display a list of all books.

    Permissions:
    - Users must have 'can_view' permission (Viewers, Editors, Admins).
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})


# View: Create a new book
# Permission: can_create
# Only users with can_create can access this page.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    """
    Create a new book entry.

    Permissions:
    - Users must have 'can_create' permission (Editors, Admins).
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('list_books')

    return render(request, 'bookshelf/create_book.html')


# View: Edit an existing book
# Permission: can_edit
# Only users with can_edit can access this page.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    """
    Edit an existing book.

    Permissions:
    - Users must have 'can_edit' permission (Editors, Admins).
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('list_books')

    return render(request, 'bookshelf/edit_book.html', {'book': book})


# View: Delete a book
# Permission: can_delete
# Only users with can_delete can access this page.
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    """
    Delete a book entry.

    Permissions:
    - Users must have 'can_delete' permission (Admins).
    """
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('list_books')

