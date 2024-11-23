from django import forms
from .models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'phone', 'instrument_type']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': "Enter the musician's first name"
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': "Enter the musician's last name"
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': "Enter email address"
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': "Enter phone number"
            }),
            'instrument_type': forms.Select(attrs={
                'placeholder': "Select the instrument type"
            }),
        }
