from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='homePage'),
    path('about/', views.about, name='aboutPage'),
    path('submit/', views.submit_form, name='submitForm'),
    path('django_form/', views.Django_form, name='django_form'),
    path('Student_form/', views.Student_form, name='Student_form'),
    path('password_form/', views.Password_Validation, name='password_form'),
]
