from rest_framework import generics, status
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class ListView(generics.ListAPIView):
    """
    GET /api/books/
    Lists all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can access


class DetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
    Retrieve a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can access


class CreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can create books

    def perform_create(self, serializer):
        # You can attach user or modify data before saving
        serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        # Custom validation logic example
        if not request.data.get("title"):
            return Response({"error": "Title is required"}, status=400)

        return super().create(request, *args, **kwargs)


class UpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/update/<id>/
    Update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Ensure only authenticated users can update books

    def update(self, request, *args, **kwargs):
        # Example: block updates for archived books
        book = self.get_object()
        if book.is_archived:
            return Response(
                {"error": "Cannot update archived book"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().update(request, *args, **kwargs)


class DeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/delete/<id>/
    Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can delete books