API Views Documentation

This project uses Django REST Framework generic views to handle CRUD operations for the Book model. Each view is designed with specific behavior, permissions, and custom logic.

### 1. ListView — List All Books

Endpoint:
GET /api/books/

Purpose:
Returns all books in the database.

Permissions:

AllowAny → Everyone can access.

Notes:
Uses DRF's built-in pagination automatically if enabled in settings.

### 2. DetailView — Retrieve One Book

Endpoint:
GET /api/books/<id>/

Purpose:
Fetch a single book using its primary key.

Permissions:

AllowAny

Notes:
DRF automatically returns 404 Not Found for invalid IDs.

### 3. CreateView — Add New Book

Endpoint:
POST /api/books/create/

Permissions:

IsAuthenticated → Only logged-in users can create books.

Custom Behavior:

create() override:
Adds custom validation for missing title.

perform_create():
Hook for attaching extra data before saving.

### 4. UpdateView — Modify Book

Endpoint:
PUT /api/books/update/<id>/
PATCH /api/books/update/<id>/

Permissions:

IsAuthenticated

Custom Behavior:

Prevents editing if book.is_archived = True.

Returns custom 403 Forbidden message.

### 5. DeleteView — Delete Book

Endpoint:
DELETE /api/books/delete/<id>/

Permissions:

IsAuthenticated

Notes:
Returns 204 No Content on success.

Custom Hooks & Settings Used

 1. perform_create(serializer)
Called after validation but before saving.
Used to attach extra fields or metadata.

 2. create(self, request, *args, **kwargs)
Overrides DRF’s default behavior to add custom validation logic.

 3. update(self, request, *args, **kwargs)
Used to enforce business rules before saving updates.

 4. Permission Classes
AllowAny for public endpoints.
IsAuthenticated for restricted write operations.