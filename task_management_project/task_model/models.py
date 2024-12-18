from django.db import models

class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)  
    assign_date = models.DateField()


    
    def __str__(self):
        return self.title