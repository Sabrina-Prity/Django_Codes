from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name = 'registration'),  
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_pass1, name='change_pass1'),
    path('set-password/', views.change_pass2, name='change_pass2'),
]
