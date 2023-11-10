from django import forms
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
