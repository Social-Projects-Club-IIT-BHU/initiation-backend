from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "index.html", context={'projects': projects})

class TestView(TemplateView):
    template_name = "/base/base.html"

class NotFoundView(TemplateView):
    template_name = "404.html"