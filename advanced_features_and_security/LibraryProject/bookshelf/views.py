from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ValidationError
from django.utils.html import escape  # SECURITY: prevents XSS by escaping unsafe HTML
from .models import Book
from .forms import ExampleForm

def book_shelf(request):
    return HttpResponse("Hello, welcome to the Bookshelf app!")

@csrf_protect
def example_form_view(request):
    """
    Secure example form:
    - CSRF-protected
    - Uses Django forms for validation (prevents SQL injection & bad input)
    - Automatically escapes output in templates (prevents XSS)
    """
    form = ExampleForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            # Clean and validated data
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            year = form.cleaned_data["publication_year"]

            # No database write needed — it's only an example
            return render(request, "bookshelf/form_example.html", {
                "form": ExampleForm(),  # show empty form again
                "success": f"Form submitted: {title} by {author} ({year})",
            })

    return render(request, "bookshelf/form_example.html", {"form": form})


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Securely display a list of books.
    - Uses Django ORM (prevents SQL injection).
    - Output auto-escaped in templates (prevents XSS).
    """
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@csrf_protect  # SECURITY: Protects against CSRF attacks
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    """
    Securely create a new book entry.
    - CSRF protection
    - Input validation
    - No raw SQL (prevents SQL injection)
    """
    if request.method == "POST":
        title = escape(request.POST.get("title", "").strip())
        author = escape(request.POST.get("author", "").strip())
        publication_year = request.POST.get("publication_year", "").strip()

        # Validate numeric year input
        if not publication_year.isdigit():
            return render(request, "bookshelf/create_book.html", {
                "error": "Publication year must be a number."
            })

        Book.objects.create(
            title=title,
            author=author,
            publication_year=int(publication_year)
        )
        return redirect("book_list")

    return render(request, "bookshelf/create_book.html")


@csrf_protect
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    """
    Securely edit a book.
    - Input validation
    - CSRF protection
    - ORM prevents SQL injection
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = escape(request.POST.get("title", "").strip())
        book.author = escape(request.POST.get("author", "").strip())
        pub_year = request.POST.get("publication_year", "").strip()

        if not pub_year.isdigit():
            return render(request, "bookshelf/edit_book.html", {
                "book": book,
                "error": "Publication year must be numeric."
            })

        book.publication_year = int(pub_year)
        book.save()

        return redirect("book_list")

    return render(request, "bookshelf/edit_book.html", {"book": book})


@csrf_protect
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    """
    Securely delete a book.
    - CSRF protected (delete buttons use POST)
    - ORM ensures safe deletion
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "bookshelf/delete_confirm.html", {"book": book})
