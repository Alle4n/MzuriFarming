from django import forms 
from .models import Crops, Users
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Check if username exists
        if username:
            if not User.objects.filter(username=username).exists():
                self.add_error('username', 'Username does not exist.')

        # Add custom password checks
        if password and len(password) < 5:
            self.add_error('password', 'Password must be at least 5 characters long.')

        return cleaned_data


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Check if passwords match
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        # Add custom password checks
        if password and len(password) < 5:
            self.add_error('password', 'Password must be at least 5 characters long.')

        return cleaned_data


class CropForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ['crop_name', 'harvest_in_kg', 'land_size_acres']  # Include new fields

    def __init__(self, *args, **kwargs):
        super(CropForm, self).__init__(*args, **kwargs)
        self.fields['crop_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'crop_name',
            'required': 'required'
        })
        self.fields['harvest_in_kg'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Harvest (kg)',
            'required': 'required'
        })
        self.fields['land_size_acres'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Land Size (acres)',
            'required': 'required'
        })