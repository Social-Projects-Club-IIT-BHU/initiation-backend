from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProjectCreateForm, UserCreationForm
from .models import Project, Requests


def index_view(request):
    projects = Project.objects.order_by('-created')[:4]
    return render(request, "index.html", context={'projects': projects})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            nexturl = request.POST.get("next", 'index')
            return redirect(nexturl)
        else:
            return render(request,
                          'login.html',
                          context={'error': 'invalid username or password'})
    return render(request, 'login.html', context={'next': ''})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'sign_up.html', context={'form': form})
    return render(request, 'sign_up.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def profile_view(request):
    return render(request, 'profile.html')


def project_list_view(request):
    projects = Project.objects.all()
    ctx = {'projects': projects}
    return render(request, 'projects_list.html', ctx)


class ProjectDetailView(DetailView):
    model = Project


class CreateProjectView(LoginRequiredMixin, View):
    template_name = 'project_form.html'
    success_url = reverse_lazy("index")

    def get(self, request):
        form = ProjectCreateForm()
        ctx = {'form': form}
        return render(self.request, self.template_name, ctx)

    def post(self, request):
        form = ProjectCreateForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(self.request, self.template_name, ctx)
        project = form.save(commit=False)
        project.submittedby = self.request.user
        project.save()
        return redirect(self.success_url)


class UpdateProjectView(LoginRequiredMixin, View):
    template_name = 'project_form.html'
    success_url = reverse_lazy("index")

    def get(self, request, pk):
        project = get_object_or_404(Project,
                                    id=pk,
                                    submittedby=self.request.user)
        form = ProjectCreateForm(instance=project)
        return render(self.request, self.template_name, {'form': form})

    def post(self, request, pk):
        project = get_object_or_404(Project,
                                    id=pk,
                                    submittedby=self.request.user)
        form = ProjectCreateForm(request.POST,
                                 request.FILES or None,
                                 instance=project)
        if not form.is_valid():
            ctx = {'form': form}
            return render(self.request, self.template_name, ctx)
        project = form.save(commit=False)
        project.save()
        return redirect(self.success_url)


class DeleteProjectView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_delete.html'

    def get_queryset(self):
        qs = super(DeleteProjectView, self).get_queryset()
        return qs.filter(submittedby=self.request.user)


def create_request(request, pk):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=pk)
        created_request = Requests(request_project=project,
                                   person=self.request.user)
        created_request.save()
        return redirect(reverse_lazy('index'))
    return redirect(reverse_lazy('index'))


def delete_request(request, pk):
    if request.method == 'POST':
        project = Project.objects.get(id=pk)
        requests = get_object_or_404(Requests,
                                     request_project=project,
                                     person=self.request.user)
        requests.delete()
        return redirect(reverse_lazy('index'))
    return redirect(reverse_lazy('index'))


class TestView(TemplateView):
    template_name = "/base/base.html"


class NotFoundView(TemplateView):
    template_name = "404.html"
