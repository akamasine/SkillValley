from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from .models import Project
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ProjectList(LoginRequiredMixin,ListView):
    model = Project
    context_object_name = 'projects'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['projects'] = context['projects'].filter(
                title__icontains=search_input)
        context['search_input'] =search_input
        return context
   
class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project
    context_object_name = 'project'

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description' ,'phone_no', 'booked']
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(ProjectCreate, self).form_valid(form)


class MyProjectList(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'authuser/myproject.html'
    context_object_name = 'myproject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myproject'] = context['myproject'].filter(user=self.request.user)
        return context


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['title', 'description' ,'phone_no', 'booked']
    success_url = reverse_lazy('myproject')

    

class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    context_object_name = 'project'
    success_url =reverse_lazy('myproject')

