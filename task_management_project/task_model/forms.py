from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter task title', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter task description', 'class': 'form-control', 'rows': 4}),
            'assign_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        
        }
