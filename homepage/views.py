from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "index.html", context={'projects': projects})
