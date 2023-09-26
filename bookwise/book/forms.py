from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        max_length=140,
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    isbn = forms.CharField(
        required=True,
        max_length=13,
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    release_year = forms.IntegerField(
        required=True,
        label="Release Year",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    name = forms.CharField(
        required=True,
        max_length=200,
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'release_year', 'authors')