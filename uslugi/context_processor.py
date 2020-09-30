from uslugi.models import Category, Meta 


def menu(request): 
    menu_list = Category.objects.filter(parent = None).order_by('sorting')
    
    menu = [] 

    for category in menu_list: 
        
        cat = Category.objects.get(title = category.title)
        children = cat.category_set.all().filter(published = True)

        if len(children) > 0:    
            menu.append( dict({ 
                'level1': cat, 
                'level2': children, 
            }))
        else: 
             menu.append( dict({ 
                'level1': cat, 
            }))
        
    return{'menu_list': menu_list, 'menu': menu}

def meta(request):
   
    try:
        meta = Meta.objects.get(slug = request.path)
        return {'meta': meta}
    except:  
        return {'meta': ''}



