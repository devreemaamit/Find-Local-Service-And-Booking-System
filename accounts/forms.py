from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'contact_number', 'address', 'username', 'email', 'role', 'password1', 'password2']

class EditProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'contact_number', 'address', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)

        # Handle password safely
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        else:
            # Prevent blank password from overriding existing one
            user.password = CustomUser.objects.get(pk=user.pk).password

        if commit:
            user.save()
        return user
