from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_shelf, name="index"),
]