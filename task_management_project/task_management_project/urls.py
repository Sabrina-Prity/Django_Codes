
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('category/', include("task_category.urls")),
    path('task/', include("task_model.urls")),
    path('edit/<int:id>/', views.edit, name='edit_task'),  
    path('delete/<int:id>/', views.delete, name='delete_task'),
    
]
