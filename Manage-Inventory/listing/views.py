from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Inventory_model
from .forms import Listing_form

# Create your views here.
def dashboard(request):
    inventory_items = Inventory_model.objects.all()
    context = {'inventory_items': inventory_items}
    return render(request, 'listing/dashboard.html', context)

def list_pdt(request):
    inventory_items = Inventory_model.objects.all()
    context = {'items': inventory_items}
    return render(request, 'listing/list.html', context)

def add(request):
    if request.method == 'POST':
        form = Listing_form(request.POST)
        if form.is_valid():
            form.save()
              # Redirect to dashboard after successful addition
    else:
        form = Listing_form()
    inventory_items = Inventory_model.objects.all()

    context = {'form': form, 'inventory_items': inventory_items}
    return render(request, 'listing/add.html', context)

def edit(request, unique_id):
    item = get_object_or_404(Inventory_model, unique_id=unique_id)
    
    if request.method == 'POST':
        form = Listing_form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = Listing_form(instance=item)
    
    context = {'form': form, 'item': item}
    return render(request, 'listing/edit.html', context)

def delete(request, unique_id):
    item = get_object_or_404(Inventory_model, unique_id=unique_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    
    context = {'item': item}
    return render(request, 'listing/delete.html', context)