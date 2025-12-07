Comment system
==============

Overview
--------
- Users can add comments to posts.
- Each comment belongs to a single Post and one User (author).
- Authors can edit or delete their comments.

How to add a comment
--------------------
- On a post detail page (e.g. /posts/<id>/), logged-in users will see a comment form.
- Fill the content and submit → you will be redirected back to the post; the comment appears in the list.

How to edit/delete a comment
----------------------------
- Only the comment's author can edit or delete it.
- Edit link leads to /comments/<comment_id>/edit/
- Delete link leads to /comments/<comment_id>/delete/

URLs
----
- Create: /posts/<post_pk>/comments/new/  (POST)
- Edit: /comments/<pk>/edit/
- Delete: /comments/<pk>/delete/

Migration
---------
1. python manage.py makemigrations blog
2. python manage.py migrate

Tests
-----
- Test adding, editing, deleting comments while logged in.
- Test that anonymous users can't add comments.
- Test that non-authors cannot edit/delete others' comments.