from django import forms   #this is used for django built in forms
from django.core import validators   #this is used for django built in validators


class contactForm(forms.Form):
    name = forms.CharField(label=("User Name"), initial="Sabrina Sultana", help_text="Total length within 50 characters", required=False)
    email = forms.EmailField(label=("User Email"), widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

    # widget ---> Field to Html input


    # Upload a file
    # file = forms.FileField()

    age = forms.IntegerField(widget=forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # Image = forms.ImageField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))

    # Choose option field
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    choose = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)

    # Choose Multiple option field
    MEAL = [('P', 'Pepperoni'), ('T', 'Tomato'), ('B', 'Beef'), ('M', 'Mushroom')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget= forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
#     # email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

#     # def clean_name(self):
#     #     valName = self.cleaned_data['name']
#     #     if len(valName) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 character")
#     #     return valName
#     # def clean_email(self):
#     #     valEmail = self.cleaned_data['email']
#     #     if '.com' not in valEmail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return valEmail
    


#     # Use ShortCut
#     name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
#     def clean(self):
#         cleaned_data = super().clean()
#         valName = self.cleaned_data['name']
#         valEmail = self.cleaned_data['email']

#         if len(valName) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 character")
        
#         if '.com' not in valEmail:
#             raise forms.ValidationError("Your email must contain .com")




# Use Django Built In Validators
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}), validators=[validators.MaxLengthValidator(10, message='Enter a name at Max 10 character')])
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}), validators=[validators.EmailValidator(message='Enter a valid email')])

    age = forms.IntegerField(validators=[validators.MaxValueValidator(34), validators.MinValueValidator(24)])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])])


# Simple password Matching Project
class Password_Validation_Project(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valName = self.cleaned_data['name']
        valPass = self.cleaned_data['password']
        val_confirm_pass = self.cleaned_data['confirm_password']

        if len(valName) < 10:
            raise forms.ValidationError("Name must be at least 10 Character")
        if valPass != val_confirm_pass:
            raise forms.ValidationError("Password does not match")
        