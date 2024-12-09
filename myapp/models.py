from django.db import models

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
     
     
     TaskName= models.CharField(max_length=100)
     Description=models.TextField()
     DueDate=models.DateField()
     date_created = models.DateTimeField(auto_now_add=True) 
 
def __str__(self):
        return self.task_name
