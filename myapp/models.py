from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Form(models.Model):
        
        name = models.CharField(max_length=100)
        description= models.TextField()




class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TaskName = models.CharField(max_length=100)
    Description = models.TextField()
    DueDate = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def time_remaining(self):
         
        if self.DueDate:
             
            due_date = timezone.datetime.combine(self.DueDate, timezone.datetime.min.time())
            due_date = timezone.make_aware(due_date)  # Make the due_date timezone-aware
        return due_date - timezone.now()  # Now both are aware
        
    

    def __str__(self):
        return self.TaskName  # Ensure the property name matches
    
class Form(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)  # Added DueDate field

    def __str__(self):
        return self.name


