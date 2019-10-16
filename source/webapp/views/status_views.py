from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.models import Status
from webapp.forms import StatusForm
from webapp.views import reverse_lazy


class StatusView(ListView):
    context_object_name = 'statuses'
    model = Status
    template_name = 'status/status_ls.html'


class StatusCreateView(CreateView):
    template_name = 'status/create_status.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_ls')


class StatusesUpdateView(UpdateView):
    model = Status
    template_name = 'status/update_status.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_ls')


class StatusesDeleteView(DeleteView):
    template_name = 'status/delete_status.html'
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('status_ls')

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return HttpResponse("<h2>This object is protected<h2/>")




