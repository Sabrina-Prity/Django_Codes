from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def registration(request):
    if request.method == 'POST':
       register_form = forms.RegistrationForm(request.POST)
       if register_form.is_valid():
           register_form.save()
           messages.success(request, 'Account Created SuccessFully')
           return redirect('registration')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'registration.html', {'form': register_form, 'type': 'Registration'})



def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name, password=password)
                if user is not None:
                    messages.success(request, 'Logged In Successfully')
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    return render(request, 'profile.html')


def change_pass1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Change Successfully')
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'change_pass.html', {'form':form})
    else:
        return redirect('user_login')
    


def change_pass2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Change Successfully')
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form =SetPasswordForm(user = request.user)
        return render(request, 'change_pass.html', {'form':form})
    else:
        return redirect('user_login')