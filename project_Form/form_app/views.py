from django.shortcuts import render
from . form import contactForm
from . form import StudentData, Password_Validation_Project
# Create your views here.
def home(request):
    return render(request, './form_app/home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './form_app/about.html', {
            'name': name,
            'email': email,
            'select' : select,
        })
    else:
        return render(request, './form_app/about.html')

def submit_form(request):
    # print(request.POST)
    return render(request, './form_app/form.html')

def Django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./form_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, './form_app/django_form.html', {'form': form})

def Student_form(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, './form_app/django_form.html', {'form': form})


def Password_Validation(request):
    if request.method == 'POST':
        form = Password_Validation_Project(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = Password_Validation_Project()
    return render(request, './form_app/django_form.html', {'form': form})