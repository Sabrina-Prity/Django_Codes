from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'musician', 'release_date', 'rating']
        widgets = {
            'album_name': forms.TextInput(attrs={
                'placeholder': 'Enter the album name.'
            }),
            'release_date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Select the release date.'
            }),
            'rating': forms.Select(attrs={
                'placeholder': 'Rate the album.'
            }),
        }
