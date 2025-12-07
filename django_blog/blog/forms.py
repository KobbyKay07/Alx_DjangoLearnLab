from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile details.
    Allows editing of username, email, and optionally additional fields like bio.
    """
    class Meta:
        model = User
        fields = ['username', 'email']


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

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment..."}),
        max_length=2000,
        help_text="Maximum 2000 characters."
    )

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content", "").strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        return content