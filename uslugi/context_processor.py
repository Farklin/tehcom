from uslugi.models import Category, Meta 


def menu(request): 
    menu_list = Category.objects.filter(parent = None)
    return{'menu_list': menu_list}

def meta(request):
   
    try:
        meta = Meta.objects.get(slug = request.path)
        return {'meta': meta}
    except:  
        return {'meta': ''}



