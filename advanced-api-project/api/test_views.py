from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from .models import Book, Author

"""
TESTING OVERVIEW
This test suite validates:

1. CRUD operations for Book model
2. Filtering, searching, and ordering
3. Permission rules (Create, Update, Delete require authentication)
4. Response data structure and status codes
"""


class BookAPITest(APITestCase):

    def setUp(self):
        """
        SETUP PHASE:
        Runs before each test.
        Creates:
            - A user for authentication tests
            - An author and two books
        """

        self.client = APIClient()

        # User for authenticated requests
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Test author
        self.author = Author.objects.create(name="John Doe")

        # Test books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Beta Book",
            publication_year=2024,
            author=self.author
        )

        # URL endpoints
        self.list_url = reverse("books-list")      # GET /books/
        self.create_url = reverse("books-create")  # POST /books/create/
        self.detail_url = reverse("books-detail", args=[self.book1.id])  # GET /books/<id>/
        self.update_url = reverse("books-update", args=[self.book1.id])
        self.delete_url = reverse("books-delete", args=[self.book1.id])


    
    # List View Test
    def test_list_books(self):
        """Test GET /books/ returns all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    
    # Detail View Test
    def test_retrieve_single_book(self):
        """Test GET /books/<id>/ returns the correct book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha Book")


    
    # Create View Tests
    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication → Forbidden"""
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Test authenticated users can create a book"""
        self.client.login(username="testuser", password="password123")

        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data["title"], "New Book")


    
    # Update View Tests
    def test_update_book_unauthenticated(self):
        """Test updating a book without logging in"""
        data = {"title": "Updated Title"}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test authenticated update works"""
        self.client.login(username="testuser", password="password123")

        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")


    
    # Delete View Tests
    def test_delete_book_unauthenticated(self):
        """Unauthenticated delete should fail"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Authenticated delete should succeed"""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())


    
    # Filtering / Search / Ordering Tests
    def test_filter_books_by_title(self):
        """Test filtering by title: ?title=Alpha"""
        response = self.client.get(self.list_url + "?title=Alpha Book")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    def test_search_books(self):
        """Test search: ?search=Alpha"""
        response = self.client.get(self.list_url + "?search=Alpha")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    def test_order_books_by_title(self):
        """Test ordering by title: ?ordering=title"""
        response = self.client.get(self.list_url + "?ordering=title")
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, ["Alpha Book", "Beta Book"])
