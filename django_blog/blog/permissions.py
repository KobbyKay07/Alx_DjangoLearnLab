from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    """
    Allows access only to the author of the post.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
