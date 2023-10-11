from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return f'{self.username}'


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True,null=True)
    start_date = models.TimeField(auto_now=True)
    end_time = models.TimeField(blank=True,null=True)
    owner = models.ForeignKey(CustomUser,on_delete= models.CASCADE,related_name='owners')
    members = models.ManyToManyField(CustomUser,related_name='members')
    
    def __str__(self):
        return f'{self.title}'
    

class Task(models.Model):
    title = models.CharField(max_length=256)   
    description = models.TextField()
    deadline_date = models.DateTimeField(blank=True,null=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'