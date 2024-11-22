from django.shortcuts import render
from . forms import ExampleForm
from first_app.forms import Model_Form
# Create your views here.

def home(request):
    return render(request, './first_app/home.html')


def Django_form(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExampleForm()
    return render(request, './first_app/django_forms.html', {'form': form})


def Model_form(request):
    if request.method == 'POST':
        form = Model_Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = Model_Form()
    return render(request, './first_app/model_forms.html', {'form': form})