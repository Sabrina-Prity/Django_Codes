from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages
from .models import Album
from django.urls import reverse_lazy
from . import forms
# Create your views here.
# Function Based View
# def add_album(request):
#     if request.method == 'POST':
#        album_form = forms.AlbumForm(request.POST)
#        if album_form.is_valid():
#            album_form.save()
#            return redirect('add_album')
#     else:
#         album_form = forms.AlbumForm()
#     return render(request, 'add_album.html', {'form': album_form})



# Class-Based View
class AddAlbumCreateView(CreateView):  
    model = Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        messages.success(self.request, "Successfully added the album!")
        form.instance.user = self.request.user
        return super().form_valid(form)