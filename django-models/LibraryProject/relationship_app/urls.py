from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.booklist, name='booklist'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail')
]