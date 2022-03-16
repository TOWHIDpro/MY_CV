from django.shortcuts import render, HttpResponseRedirect
from . forms import TodoForm
from . models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/enroll/login")
def todo(request):
    return render(request, 'todo/todo.html')

def details(request, id_number):
    return render(request, 'todo/details.html')

