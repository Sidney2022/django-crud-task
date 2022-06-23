from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import TodoApp

class TodoAppCreateView(CreateView):
       model = TodoApp
       fields = [
              'title',
              'description'
       ]
       template_name = 'home.html'
