
from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.AddMusicianCreateView.as_view(), name = 'add_musician'),
    # path('add/', views.add_musician, name = 'add_musician'),
]
