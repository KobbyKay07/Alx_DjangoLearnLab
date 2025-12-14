from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    # Posts
    path("posts/", PostListCreateView.as_view(), name="post_list_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    # Comments
    path("posts/<int:post_id>/comments/", CommentListCreateView.as_view(), name="comment_list_create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment_detail"),
]
