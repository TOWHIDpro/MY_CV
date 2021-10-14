from django.shortcuts import render, HttpResponseRedirect, redirect
from . models import User
from . forms import StudentRegistration
from django.http import JsonResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            stu = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (stu == ''):
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=stu, name=name, email=email, password=password)
            usr.save()

            stu_deta = list(User.objects.values())
            return JsonResponse({'status':'save', 'stu_deta':stu_deta})
        else:
            return JsonResponse({'status':0})

    else:
        fm = StudentRegistration()
    studata = User.objects.all()
    return render(request, 'crud/crud.html', {
        'form': fm,
        'students': studata
    })



def update_data(request):
    if request.method == 'POST':  
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)
        stu_deta = {'id':pi.id, 'name':pi.name, 'email':pi.email, 'pass':pi.password}
        return JsonResponse({'status':'ok', 'stu_deta':stu_deta})
    else:
        return JsonResponse({'status':0})





def delete(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':'delete'})
    else:
        return JsonResponse({'status':0})
