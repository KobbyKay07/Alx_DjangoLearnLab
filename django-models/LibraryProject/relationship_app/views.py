from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView

# Create your views here.
def booklist(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, "relationship_app/booklist.html", context)