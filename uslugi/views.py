

from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Uslusgi

def view_categoryes(request):
    categoryes = Category.objects.all()
    return render(request, 'uslugi/index.html', {'categoryes': categoryes})

def view_category(request,slug ): 
    category = Category.objects.get(slug = slug)
    uslugies = category.uslusgi_set.all()
    return render(request, 'uslugi/category.html', {'category':category, 'uslugies':uslugies})

def view_uslugi(request, slug_category, slug_uslugi): 
    uslugi = Uslusgi.objects.get(slug = slug_uslugi)
    parent_category = uslugi.parent_category
    return render(request, 'uslugi/uslugi.html', {'uslugi':uslugi, 'parent_category': parent_category})