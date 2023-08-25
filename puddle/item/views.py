from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import NewItemForm, EditItemForm
from .models import Item, Category

def items(request):
  query = request.GET.get('query','')
  items = Item.objects.filter(is_sold=False)
  categories = Category.objects.all()
  category_id = request.GET.get('category', 0)
  
  if category_id:
    items = items.filter(category_id=category_id) 
  
  if query:
    items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
  
  return render(request, 'item/items.html', {'items': items, 'query': query, 'categories': categories, 'category_id': int(category_id)})

def detail(request, item_id): 
  item = get_object_or_404(Item, pk=item_id)
  related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item_id)[:3]
  
  return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})

@login_required
def new(request):
  if request.method == 'POST':
    form = NewItemForm(request.POST, request.FILES)
    if form.is_valid():
      item = form.save(commit=False)
      item.created_by = request.user
      item.save()
      return redirect('item:detail', item_id=item.id)
  else:
    form = NewItemForm()
  
  return render(request, 'item/form.html', {'form': form, 'title': 'New Item'})

@login_required
def edit(request, item_id):
  item = get_object_or_404(Item, pk=item_id, created_by=request.user)
  
  if request.method == 'POST':
    form = EditItemForm(request.POST, request.FILES, instance=item)
    if form.is_valid():
      form.save()
      return redirect('item:detail', item_id=item.id)
  else:
    form = EditItemForm(instance=item)
  
  return render(request, 'item/form.html', {'form': form, 'title': 'Edit Item'})


@login_required
def delete(request, item_id):
  item = get_object_or_404(Item, pk=item_id, created_by=request.user)
  item.delete()
  return redirect('dashboard:index')