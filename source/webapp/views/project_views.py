from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.models import Project
from webapp.forms import ProjectForm


class ProjectView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project/project_ls.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


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

#
# class TaskTrackerUpdateView(UpdateView):
#     model = Tracker
#     template_name = 'tracker/update.html'
#     form_class = TrackerForm
#     context_object_name = 'task_tracker'
#
#     def get_success_url(self):
#         return reverse('task_track', kwargs={'pk': self.object.pk})
#
#
# class TaskTrackerDeleteView(DeleteView):
#     template_name = 'tracker/delete.html'
#     model = Tracker
#     context_object_name = 'task_tracker'
#     success_url = reverse_lazy('index')
