from django import forms
from .models import Crops, Users

class CropForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ['CropName', 'ScientificName', 'AverageYield']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'scientific_name': forms.TextInput(attrs={'class': 'form-control'}),
            'average_yield': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['Username', 'Password', 'Email', 'Role']