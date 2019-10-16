from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.models import Project, Tracker
from webapp.forms import ProjectForm, TrackerForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TrackerForm()
        trackers = context['project'].tracker.order_by('-created_at')
        self.paginate_comments_to_context(trackers, context)
        return context

    def paginate_comments_to_context(self, trackers, context):
        paginator = Paginator(trackers, 8)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['trackers'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


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
