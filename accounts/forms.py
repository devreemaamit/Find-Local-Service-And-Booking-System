from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'email', 'role', 'password1', 'password2']
