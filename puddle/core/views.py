from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth import logout as auth_logout

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:15]
    categories = Category.objects.all()
    return render(request, 'core/index.html', context={'items': items, 'categories': categories})

def contact(request):
    return render(request, 'core/contact.html')

def policy(request):
    return render(request, 'core/policy.html')

def termsOfUse(request):
    return render(request, 'core/termsofuse.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
        
    return render(request, 'core/signup.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/login/')