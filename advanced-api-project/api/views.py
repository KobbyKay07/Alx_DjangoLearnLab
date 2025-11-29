from rest_framework import generics, status, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ListView(generics.ListAPIView):
    """
    GET /api/books/
    Displays a list of all books.

    Features:
    - Filtering: Users can filter by title, author name, and publication_year.
    - Searching: Allows text-based search on title and author's name.
    - Ordering: Users can order results by title, publication_year, or author.
    - Permissions: Read-only access for unauthenticated users.

    Custom behavior:
    - Uses DjangoFilterBackend for flexible field-based filtering.
    - Uses SearchFilter for partial text matching.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields users can filter by
    filterset_fields = ['title', 'author', 'publication_year']

    # Searchable fields
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    odering_fields = ['title', 'publication_year']
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can access


class DetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/
     Retrieves a single book based on its primary key.

    Permissions:
    - Fully open for reading.
    - Write operations handled by other views.

    Custom behavior:
    - DRF automatically fetches the correct book instance using the pk from the URL.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can access


class CreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Allows authenticated users to create new book entries.

    Features:
    - Enforces authentication.
    - Uses serializer validation to ensure valid input data.

    Custom behavior:
    - Can be extended with additional logic such as:
        * Automatically assigning request.user as creator
        * Pre-save hooks in serializer
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
    Updates an existing book instance.

    Features:
    - Only authenticated users can update books.
    - Partial updates supported (PATCH).

    Custom behavior:
    - Override perform_update() if you need custom update behavior
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
    Deletes a book instance.

    Features:
    - Restricted to authenticated users only.

    Custom behavior:
    - Override perform_destroy() to log deletions or cascade operations.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can delete books