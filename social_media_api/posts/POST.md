# 📘 Posts & Comments API Documentation

This document describes how to interact with the **Posts** and **Comments** endpoints of the Social Media API, including authentication, pagination, filtering, and example requests and responses.

---

## 🔐 Authentication

This API uses **Token Authentication**.

### Obtain Token
POST /accounts/login/

bash
Copy code

#### Request
```json
{
  "email": "user@example.com",
  "password": "password123"
}
Response
json
Copy code
{
  "token": "abc123xyz"
}
Using the Token
Include the token in request headers:

makefile
Copy code
Authorization: Token abc123xyz
📝 Posts Endpoints
List Posts (Paginated & Searchable)
sql
Copy code
GET /posts/
GET /posts/?search=django
GET /posts/?page=2
Response
json
Copy code
{
  "count": 15,
  "next": "http://localhost:8000/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Learning Django",
      "content": "Django is powerful...",
      "author": "john_doe",
      "created_at": "2025-01-10T12:00:00Z",
      "updated_at": "2025-01-10T12:00:00Z",
      "comments_count": 2
    }
  ]
}
Create a Post (Authenticated)
bash
Copy code
POST /posts/
json
Copy code
{
  "title": "My First Post",
  "content": "This is my first post."
}
Retrieve a Single Post
bash
Copy code
GET /posts/<post_id>/
json
Copy code
{
  "id": 1,
  "title": "Learning Django",
  "content": "Django is powerful...",
  "author": "john_doe",
  "created_at": "2025-01-10T12:00:00Z",
  "updated_at": "2025-01-10T12:00:00Z"
}
Update a Post (Author Only)
bash
Copy code
PUT /posts/<post_id>/
json
Copy code
{
  "title": "Updated Title",
  "content": "Updated content"
}
Delete a Post (Author Only)
bash
Copy code
DELETE /posts/<post_id>/
💬 Comments Endpoints
List Comments for a Post (Paginated)
bash
Copy code
GET /posts/<post_id>/comments/
json
Copy code
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 5,
      "post": 1,
      "author": "jane_doe",
      "content": "Great post!",
      "created_at": "2025-01-12T10:15:00Z",
      "updated_at": "2025-01-12T10:15:00Z"
    }
  ]
}
Create a Comment (Authenticated)
bash
Copy code
POST /posts/<post_id>/comments/
json
Copy code
{
  "content": "Very helpful post!"
}
Update a Comment (Author Only)
bash
Copy code
PUT /comments/<comment_id>/
json
Copy code
{
  "content": "Updated comment content."
}
Delete a Comment (Author Only)
bash
Copy code
DELETE /comments/<comment_id>/
🔎 Search & Filtering
Posts can be searched by title and content:

sql
Copy code
GET /posts/?search=django
📄 Pagination
Pagination is enabled for both posts and comments.

Pagination Fields
count

next

previous

results

Default page size: 10

🔐 Permissions Summary
Action	                              Permission
View posts & comments	              Public
Create post/comment	                  Authenticated
Update/Delete post	                  Post author only
Update/Delete comment	              Comment author only

✅ Testing Checklist
List posts and comments

Create posts and comments while authenticated

Ensure anonymous users cannot create content

Verify authorship restrictions

Confirm pagination and search functionality

📌 Notes
All write operations require authentication

Unauthorized actions return 403 Forbidden

Invalid data returns 400 Bad Request