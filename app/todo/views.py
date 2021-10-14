import django
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from . forms import TodoForm
from . models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/enroll/login")
def todo(request):
    form = TodoForm(request.GET)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return HttpResponseRedirect('/todo')
    else:
        form = TodoForm()
    datas = Todo.objects.filter(user=request.user)
    return render(request, 'todo/todo.html', {
        'form': form,
        'user': request.user,
        'datas': datas
    })

def details(request, id_number):
    data = Todo.objects.get(id=id_number, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=data)
        form.save()
        return render(request, 'todo/details.html', {
        'form': form,
        'data':data
    })


    form = TodoForm(instance=data)
    return render(request, 'todo/details.html', {
        'form': form,
        'data':data
    })



def delete_tasks(request, id_number):
    try:
        data = Todo.objects.get(pk=id_number)
        data.delete()
    except:
        return HttpResponseRedirect('/todo/')
    return HttpResponseRedirect('/todo/')
