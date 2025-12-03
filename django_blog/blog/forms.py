from django import forms
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile details.
    Allows editing of username, email, and optionally additional fields like bio.
    """
    class Meta:
        model = User
        fields = ['username', 'email']