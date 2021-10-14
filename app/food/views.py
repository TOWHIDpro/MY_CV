from django.shortcuts import redirect, render
from . models import Item
from . forms import ItemForm
from django.contrib import messages
# Create your views here.

def index(request):
    item = Item.objects.all()
    return render(request, 'food/index.html', {
        'items': item
    })

def details(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'food/details.html', {
        'item': item
    })

def add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Item Added Succesfully')
            return redirect('food:index')
    else:
        form = ItemForm()
    
    return render(request, 'food/add.html', {
        'form': form
    })


def edit(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, 'Item Edit Succesfully')
    else:
        form = ItemForm(instance=item)
    return render(request, 'food/edit.html', {
        'form': form,
        'item': item
    })

def delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('food:index')