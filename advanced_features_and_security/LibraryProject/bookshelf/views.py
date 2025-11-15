from django.shortcuts import HttpResponse

# Create your views here.
def book_shelf(request):
    return HttpResponse("Hello, welcome to the Bookshelf app!")
