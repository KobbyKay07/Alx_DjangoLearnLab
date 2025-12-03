Django Blog Authentication Documentation
1. Overview

The authentication system allows users to:

Register new accounts

Log in and log out

Manage and update profile information

It uses:

Django’s built-in authentication system for login/logout

Custom user registration form extending UserCreationForm

Custom profile management view for editing user data

2. URL Routes
URL Path	HTTP Method	Purpose	Authentication Required
/register/	GET, POST	Display registration form & create account	No
/login/	GET, POST	Display login form & authenticate user	No
/logout/	GET	Logs out the current user	Yes
/profile/	GET, POST	View and update user profile	Yes
3. Forms
3.1 Registration Form

Class: CustomUserCreationForm

Base: UserCreationForm

Fields:

username

email

password

Optional: profile_picture, bio

Behavior:

Validates password match

Ensures unique username and email

Creates a new user on successful submission

3.2 Profile Form

Class: UserProfileForm

Base: forms.ModelForm

Fields:

username

email


Behavior:

Pre-fills with current user data

Updates user instance on submission

Requires authentication

4. Views
4.1 Registration View

URL: /register/

Type: Class-based

Behavior:

GET → display empty form

POST → validate & create user, redirect to login

4.2 Login View

URL: /login/

Type: Django’s LoginView

Behavior:

Authenticates user credentials

Creates a session on success

Displays errors on failure

4.3 Logout View

URL: /logout/

Type: Django’s LogoutView

Behavior:

Clears user session

Redirects to login or homepage

4.4 Profile View

URL: /profile/

Type: Custom view

Behavior:

GET → display form with user data

POST → validate & update user

Requires authentication

5. Templates

Base template: base.html
Contains navigation links: Home, Blog Posts, Login, Register, Profile, Logout

Login template: login.html

Register template: register.html

Profile template: profile.html

Logout: Optional confirmation page or automatic redirect

Each template uses {% csrf_token %} for security and {% block content %} for page-specific content.

6. Permissions and Security

Passwords hashed using Django’s default hasher

CSRF protection enabled on all POST forms

/profile/ and /logout/ require user authentication

Optional: enforce strong password validation and email uniqueness

Optional: extend User model for extra fields like profile_picture or bio

7. Testing Instructions

Run the server:

python manage.py runserver


Register a new user via /register/

Login using /login/ with valid credentials

Access profile at /profile/ and update details

Logout via /logout/

Test access restrictions: Try /profile/ while logged out → should redirect to /login/

8. Example Workflow

User visits /register/ → submits form → account created

User logs in at /login/ → session created

User updates email or profile → changes saved at /profile/

User logs out → session cleared

Unauthorized users cannot access /profile/ or /logout/