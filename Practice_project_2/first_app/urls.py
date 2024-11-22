from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='homePage'),
    path('django_form/', views.Django_form, name = 'django_form'),
    path('model_form/', views.Model_form, name = 'model_form'),
]
