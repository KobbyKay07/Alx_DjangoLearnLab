from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
    tag_names = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tag_names']
        widgets = {'tags':TagWidget(attrs={'data-role':'tagsinput'})}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)

        if self.user:
            post.author = self.user

        if commit:
            post.save()

        raw_tags = self.cleaned_data.get("tag_names", "")
        tag_list = [t.strip() for t in raw_tags.split(',') if t.strip()]

        post.tags.set(tag_list)

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