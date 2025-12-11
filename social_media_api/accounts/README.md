📘 Social Media API — Django REST Framework

A simple social media backend built with Django, Django REST Framework, and SimpleJWT.
It features:

Custom user model with profile picture

User bio

Followers system

JWT authentication

Endpoints for registration, login, and profile management

🚀 Features

Custom CustomUser model extending AbstractUser

User registration with password hashing

Login with JWT tokens (access + refresh)

Follow/unfollow system

Upload profile pictures

Update profile (bio, email, username, picture)

DRF-based API views and serializers

📦 Tech Stack

Python 3.12+

Django 5+

Django REST Framework

SimpleJWT

Pillow (for image uploads)

📁 Project Setup

Follow these steps to run the project locally.

1. Clone the Repository
git clone https://github.com/yourusername/social_media_api.git
cd social_media_api

2. Create a Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt


Make sure your requirements include:

Django
djangorestframework
djangorestframework-simplejwt
Pillow

4. Configure the Custom User Model

In your settings.py, ensure:

AUTH_USER_MODEL = 'accounts.CustomUser'


This must be set before running migrations.

5. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser
python manage.py createsuperuser

7. Start the Server
python manage.py runserver


Your API is now running at:

http://127.0.0.1:8000/

👤 Custom User Model Overview

The API uses a custom model:

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name="following", blank=True)

✔ Features:

Inherits all default Django authentication fields

Adds bio, profile_picture

Adds followers relationship

Supports authentication via JWT

Can be serialized through DRF serializers

🔑 Authentication (JWT)

Authentication is handled using SimpleJWT.

Endpoints:

Purpose	Method	URL
Obtain JWT access + refresh token	POST	/api/auth/login/
Refresh access token	POST	/api/auth/token/refresh/
🔐 Login Example

Request:

{
  "username": "testuser",
  "password": "password123"
}


Response:

{
  "refresh": "eyJ0eXA....",
  "access": "eyJ0eXAiOi...."
}


Use your access token in headers:

Authorization: Bearer <your_access_token>

📝 Registration

Endpoint:

POST /api/auth/register/


Example request:

{
  "username": "ampadu",
  "email": "test@example.com",
  "password": "Password123!",
  "bio": "Software engineer",
  "followers": []
}


Example response:

{
  "id": 1,
  "username": "ampadu",
  "email": "test@example.com",
  "bio": "Software engineer",
  "profile_picture": null
}

🔄 Followers System
Follow a user
POST /api/users/<id>/follow/

Unfollow a user
POST /api/users/<id>/unfollow/

Get followers
GET /api/users/<id>/followers/

Get following
GET /api/users/<id>/following/

🧩 Project Structure
accounts/
│── models.py        # CustomUser model
│── serializers.py   # UserSerializer, RegisterSerializer
│── views.py         # RegisterView, LoginView, UserProfileView
│── urls.py          # Authentication routes
│── permissions.py   # Custom permission classes
│── ...
social_media_api/
│── settings.py
│── urls.py
│── ...

✔ Example API Endpoints
Endpoint	                Method	         Description
/api/auth/register/	        POST	         Create a new user
/api/auth/login/	        POST	         Get JWT tokens
/api/auth/token/refresh/	POST	         Refresh token
/api/users/me/	            GET	             Retrieve your profile
/api/users/me/	            PUT	             Update profile
/api/users/<id>/	        GET	             Get another user's profile
/api/users/<id>/follow/	    POST	         Follow a user
/api/users/<id>/unfollow/	POST	         Unfollow a user