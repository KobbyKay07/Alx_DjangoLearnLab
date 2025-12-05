from django import forms
from django.contrib.auth.models import User
from .models import Post

class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile details.
    Allows editing of username, email, and optionally additional fields like bio.
    """
    class Meta:
        model = User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] # Exclude 'author' to set it automatically

    def __init__(self, *args, **kwargs):
        # Pass the logged-in user to the form
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        if self.user:
            post.author = self.user     # Automatically assign the logged-in user
        if commit:
            post.save()
        return post
