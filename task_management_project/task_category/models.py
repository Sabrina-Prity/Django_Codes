from django.db import models
from task_model.models import TaskModel

# Create your models here.
class TaskCategory(models.Model):
   
    category_name = models.CharField(max_length=255)
    task_model = models.ManyToManyField(TaskModel, null=True, blank=True)

   
    
    def __str__(self):
        return self.category_name