from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages
from .models import Musician
from django.urls import reverse_lazy
from . import forms

# Create your views here.
# def add_musician(request):
#     if request.method == 'POST':
#        musician_form = forms.MusicianForm(request.POST)
#        if musician_form.is_valid():
#            musician_form.save()
#            return redirect('add_musician')
#     else:
#         musician_form = forms.MusicianForm()
#     return render(request, 'add_musician.html', {'form': musician_form})



# Class-Based View
class AddMusicianCreateView(CreateView):  
    model = Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        messages.success(self.request, "Successfully added Musician!")
        form.instance.user = self.request.user
        return super().form_valid(form)


