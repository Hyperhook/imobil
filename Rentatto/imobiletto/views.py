from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from imobiletto.models import Proprietario

class ProprietarioList(ListView):
	model = Proprietario
	template_name = 'proprietario_list.html'

class ProprietarioCreate(CreateView):
	model = Proprietario
	fields = ['nome', 'documento']
	template_name = 'proprietario_form.html'
	success_url = 'proprietario_list.html'

class ProprietarioUpdate(UpdateView):
	model = Proprietario

class ProprietarioDelete(DeleteView):
	model = Proprietario