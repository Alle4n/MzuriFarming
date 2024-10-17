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
    classification = forms.CharField(  # Change this to a CharField
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Crop Classification"
    )

    class Meta:
        model = Crops
        fields = ['crop_name', 'scientific_name', 'average_yield', 'classification']  # Use lowercase field names to match model

        widgets = {
            'crop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'scientific_name': forms.TextInput(attrs={'class': 'form-control'}),
            'average_yield': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_average_yield(self):
        average_yield = self.cleaned_data.get('average_yield')
        if average_yield is not None and average_yield < 0:
            raise ValidationError("Average yield must be a positive number.")
        return average_yield
