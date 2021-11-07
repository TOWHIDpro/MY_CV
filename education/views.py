from django.shortcuts import render
from . models import Subject, Gallery, Middle_text

# Create your views here.

def index(request):
    sub_data = Subject.objects.all()
    images = Gallery.objects.all()
    text = Middle_text.objects.first()
    return render(request, 'education/index.html', {
        'sub_data':sub_data,
        'images':images,
        'text': text
    })

def details(request, slug):
    sub_data = Subject.objects.get(slug=slug)
    return render(request, 'education/columns.html', {
        'sub_data':sub_data
    })