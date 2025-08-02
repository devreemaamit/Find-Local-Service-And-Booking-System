from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'contact_number', 'address', 'username', 'email', 'role', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if CustomUser.objects.filter(contact_number=contact_number).exists():
            raise ValidationError("Contact number already exists.")
        return contact_number

class EditProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'contact_number', 'address', 'password']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.instance = kwargs.get('instance')  # user being edited

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This email is already in use.")
        return email

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if CustomUser.objects.filter(contact_number=contact_number).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This contact number is already in use.")
        return contact_number

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        else:
            user.password = CustomUser.objects.get(pk=user.pk).password

        if commit:
            user.save()
        return user

