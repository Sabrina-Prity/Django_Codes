from django import forms
from django.forms.widgets import NumberInput
from first_app.models import ModelForm

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'row':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    
    # Single Choice Field
    # favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    # Multiple Choice Field
    # favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

class Model_Form(forms.ModelForm):
    
    class Meta:
        model = ModelForm
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : "Student Roll"
        }
        widgets  = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write your full name"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }
