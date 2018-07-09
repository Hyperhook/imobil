from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Proprietario


class ProprietarioList(ListView):
    model = Proprietario
    template_name = 'proprietario_list.html'


class ProprietarioCreate(CreateView):
    model = Proprietario
    fields = ['nome', 'documento']
    template_name = 'proprietario_form.html'

    def get_success_url(self):
        return reverse_lazy('proprietarios:proprietario-view')


class ProprietarioUpdate(UpdateView):
    model = Proprietario


class ProprietarioDelete(DeleteView):
    model = Proprietario
