from django import forms
from .models import TaskCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'

        widgets = {
            'category_name': forms.TextInput(attrs={'placeholder': 'Enter category name', 'class': 'form-control'}),
        }