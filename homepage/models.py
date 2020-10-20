from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    submittedby = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Forum(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    projectname = models.CharField(max_length=100)

class Chat(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    text = models.SlugField()
    time = models.DateTimeField(auto_now_add=True)
