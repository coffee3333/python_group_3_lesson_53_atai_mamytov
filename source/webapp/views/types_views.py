from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from webapp.models import Type
from webapp.forms import TypeForm
from webapp.views import UpdateView, DeleteView, reverse_lazy


class TypeView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/types_ls.html'


class TypesCreateView(CreateView):
    template_name = 'type/create_type.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_ls')


class TypesUpdateView(UpdateView):
    model = Type
    template_name = 'type/update_type.html'
    form_class = TypeForm
    context_key = 'type'

    def get_redirect_url(self):
        return reverse('type_ls')


def type_delete_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        return render(request, 'type/delete_type.html', context={'type': type})
    elif request.method == 'POST':
        type.delete()
        return redirect('type_ls')


class TypeDeleteView(DeleteView):
    template_name = 'type/delete_type.html'
    model = Type
    context_object_name = 'type'
    success_url = reverse_lazy('type_ls')

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return HttpResponse("<h2>This object is protected<h2/>")
