from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.models import Project
from webapp.forms import ProjectForm


class ProjectView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/project_ls.html'
    ordering = ['created_at']


class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    context_key = 'project'
    model = Project
    key_kwarg = 'pk'


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_ls')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'
    success_url = reverse_lazy('project_ls')


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_ls')
