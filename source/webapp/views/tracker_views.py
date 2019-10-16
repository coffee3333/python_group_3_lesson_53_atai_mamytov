from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.models import Tracker
from webapp.forms import TrackerForm


class IndexView(ListView):
    context_object_name = 'trackers'
    model = Tracker
    template_name = 'tracker/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class TaskTrackerView(DetailView):
    template_name = 'tracker/TaskTrack.html'
    context_key = 'tracker'
    model = Tracker
    key_kwarg = 'pk'


class TaskTrackerCreateView(CreateView):
    template_name = 'tracker/create.html'
    model = Tracker
    form_class = TrackerForm

    def get_success_url(self):
        return reverse('task_track', kwargs={'pk': self.object.pk})


class TaskTrackerUpdateView(UpdateView):
    model = Tracker
    template_name = 'tracker/update.html'
    form_class = TrackerForm
    context_object_name = 'task_tracker'

    def get_success_url(self):
        return reverse('task_track', kwargs={'pk': self.object.pk})


class TaskTrackerDeleteView(DeleteView):
    template_name = 'tracker/delete.html'
    model = Tracker
    context_object_name = 'task_tracker'
    success_url = reverse_lazy('index')

