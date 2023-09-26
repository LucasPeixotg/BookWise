from django import forms
from .models import Library

class LibraryForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    
    class Meta:
        model = Library
        fields = ('name',)