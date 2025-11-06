from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

# Create your views here.
def booklist(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'