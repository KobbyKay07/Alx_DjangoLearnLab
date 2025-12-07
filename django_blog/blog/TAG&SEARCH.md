TAG & SEARCH SYSTEM

======================

Tag System
Overview

Tags allow categorizing posts for easier filtering and navigation.

Each Post can have multiple Tags.

Each Tag can belong to multiple Posts (many-to-many).

Users add tags through a comma-separated field when creating or editing a post.

Clicking on a tag shows all posts associated with that tag.

How to add tags to a post

In the Post form, enter tags in the tag_names field as a comma-separated list.

Example:

django, python, backend


New tags are automatically created if they don’t already exist.

Tags are attached to the post on save.

How tags are displayed

On a post detail page, all tags appear under the post.

Each tag is clickable.

Clicking a tag loads all posts containing that tag.

Example display:

Tags: django | python | backend

How to view posts by tag

Each tag links to:

/tags/<tag_name>/


This page lists all posts that include the selected tag.

URLs (Tag System)

View posts by tag:

/tags/<tag_name>/

Tag Migrations

Update the Post model with a Tag field (TaggableManager or ManyToManyField).

Run:

python manage.py makemigrations blog
python manage.py migrate

Tag Tests

Test adding tags during post creation.

Test editing posts to update tags.

Test automatic tag creation.

Test correct tag display on Post detail page.

Test clicking a tag filters posts properly.

Test tag search integration (see below).

Search System

================

Overview

Users can search posts using a search bar.

Search matches against:

Post titles

Post content

Tag names

Search results are displayed on a dedicated results page.

How the search works

User submits a query via:

/search/?q=<keyword>


The backend filters posts using Django’s Q lookups, e.g.:

Q(title__icontains=query) |
Q(content__icontains=query) |
Q(tags__name__icontains=query)


Results are unique using .distinct().

Search Input in Templates

Example:

<form action="/search/" method="get">
    <input type="text" name="q" placeholder="Search posts...">
</form>

Search Results Page

Displays all matched posts.

Shows message if no results are found.

Shows query used (e.g., “Results for: django”).

URLs (Search System)

Search page:

/search/

Search Tests

Test search by title.

Test search by content.

Test search by tag name.

Test empty search returns no results.

Test search results page renders correctly.

Test case-insensitive matching.