from django.shortcuts import render, get_object_or_404, redirect
from.models import Item
from.forms import ItemForm
# Create your views here.

#list the items in the models
def item_list(request):
    items=Item.objects.all()
    return render(request, 'item_list.html',{'items':items})

#create new item to the model
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

        
#for edit the item from the models

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

        
#for delete the item from models


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html',{'item':item})
            
    
