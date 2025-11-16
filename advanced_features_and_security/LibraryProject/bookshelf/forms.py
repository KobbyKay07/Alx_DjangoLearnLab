from django import forms

class ExampleForm(forms.Form):
    """
    A simple example form demonstrating:
    - Secure user input handling
    - Built-in Django validation
    - Protection against invalid input
    """

    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter title"})
    )

    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter author"})
    )

    publication_year = forms.IntegerField(
        required=True,
        min_value=0,
        max_value=2100,
        help_text="Enter a valid year between 0 and 2100"
    )

    # Extra security example: custom validation
    def clean_title(self):
        title = self.cleaned_data.get("title", "")
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid characters detected.")
        return title