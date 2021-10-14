from django.shortcuts import render
from . models import AddImage

# Create your views here.

def gallery(request):
    all_img = AddImage.objects.all()
    return render(request, 'photo_gallery/index.html', {
        'all_post': all_img
    })

def details(request, slug):
    post = AddImage.objects.get(slug = slug)
    random_p = AddImage.objects.order_by('?')[0:10]
    return render(request, 'photo_gallery/post.html',{
        'post': post,
        'random': random_p
    })