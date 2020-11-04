from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from .models import Category, Uslusgi, Article, ApplicationForm 
from django.views.decorators.http import require_GET
from django.urls import reverse 


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
        "Disallow: *.js", 
        
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def view_categoryes(request):
    categoryes = Category.objects.filter(parent = None)
    return render(request, 'uslugi/index.html', {'categoryes': categoryes})

def view_category(request,slug): 
    try: 
        category = Category.objects.get(slug = slug, parent = None)
        uslugies = category.uslusgi_set.all()
        
        try:
            children_category = Category.objects.filter(parent = category, published = True)
            if children_category == None: 
                children_category = ''
        except: 
            children_category = '' 
        
        return render(request, 'uslugi/category.html', {'category':category, 'uslugies':uslugies, 'children_category': children_category})

    except: 
        artitcle = Article.objects.get(slug = slug)
        return render(request, 'uslugi/article.html', {'article': artitcle})


def view_uslugi(request, slug_category, slug_uslugi): 
    uslugi = Uslusgi.objects.get(slug = slug_uslugi)
    parent_category = uslugi.parent_category
    return render(request, 'uslugi/uslugi.html', {'uslugi':uslugi, 'parent_category': parent_category})

def view_children_category(request, slug_category, slug_uslugi): 
    try:
        category = Category.objects.get(slug = slug_category)
        children_category = category.category_set.get(slug = slug_uslugi)
        return render(request, 'uslugi/category.html', {'category':children_category, 'parent_category': category})
    except:
        raise Http404 


def application(request): 
    try: 
        name = request.POST['name'] 
        comment = request.POST['comment']
        phone = request.POST['phone']
        if name != '' and comment != '' and phone != '': 
            application = ApplicationForm() 
            application.name = name
            application.phone = phone
            application.comment = comment
            application.save() 
            return render(request, 'uslugi/application.html')
        else: 
            return render(request, '404.html')
    except: 
        raise Http404

    




def e_handler404(request, exception): 
    return render(request, '404.html')

