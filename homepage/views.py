from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from .models import Project


def index_view(request):
    projects = Project.objects.all()
    return render(request, "index.html", context={'projects': projects})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request,
                          'login.html',
                          context={'error': 'invalid username or password'})
    return render(request, 'login.html')


def signup_view(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('index')


def profile_view(request):
    return render(request, 'profile.html')


class TestView(TemplateView):
    template_name = "/base/base.html"


class NotFoundView(TemplateView):
    template_name = "404.html"
