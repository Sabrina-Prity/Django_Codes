
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path('smart_app/', include('smart_app.urls')),
    
]
