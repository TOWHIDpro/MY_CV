from django.shortcuts import render
from . models import *
from . forms import MessageForm

# Create your views here.

def index(request):
    home        = A_Home.objects.first()
    about       = B_About.objects.first()
    skil_text   = C_Skil_text.objects.first()
    skils       = D_Skil.objects.all()
    resume      = E_resume_text.objects.first()
    summ        = F_Summary.objects.all()
    educa       = G_Education.objects.all()
    serv_txt    = H_Services_text.objects.first()
    serv        = I_Services.objects.all()
    p_folio_txt = J_Portfolio_text.objects.first()
    p_folio     = K_Portfolio.objects.all()
    cont        = L_Contact.objects.first()
    link        = A_Links.objects.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()  
    else:
        form = MessageForm()
    
    
    # form = MessageForm()  
    return render(request, 'index/home.html', {
        'home'     : home,
        'link'     : link,
        'about'    : about,
        'skil_text': skil_text,
        'skil'     : skils,
        'resume'   : resume,
        'summary'  : summ,
        'education': educa,
        'serv_text': serv_txt,
        'serv'     : serv,
        'p_folio_t': p_folio_txt,
        'p_folio'  : p_folio,
        'contact'  : cont,
        'form'     : form,
        'name'     : request.user

    })