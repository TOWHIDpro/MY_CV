from django.shortcuts import render
from . forms import PassForm
import random

# Create your views here.

def passgen(request):
    if request.method == 'POST':
        form = PassForm(request.POST)
        
        try:
            length = int(request.POST.get('length'))
        except:
            length = 8
        
    

        lowchar = list('abcdefghijklmnopqrstwxyz')
        upchar = list('ABCDEFGHIJKLMNOPQRSTWXYZ')
        num = list('1234567890')
        spl_char = list('!@#$%^&*()')

   
        
    
        if request.POST.get('upper'):
            lowchar.extend(upchar)
        if request.POST.get('numbers'):
            lowchar.extend(num)
        if request.POST.get('char'):
            lowchar.extend(spl_char)



        thepass = ''
        for x in range(length):
            thepass += random.choice(lowchar)

            
    else:
        form = PassForm()
        thepass = ''
    return render(request, 'pass_gen/passgen.html', {
        'form':form,
        'password': thepass
    })