from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        required=True, 
        max_length=100,
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-2",
            }
        )
    )
    password1 = forms.CharField(
        required=True, 
        max_length=100,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    password2 = forms.CharField(
        required=True, 
        max_length=100,
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password1", "password2"]