from django.contrib import admin
from .models import Category
from .models import Uslusgi, Meta

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources 
from import_export import fields 
from import_export.widgets import ForeignKeyWidget

class GenerateUrlChPU(resources.ModelResource):
    prepopulated_fields = {'slug': ('title',)}
    parent = fields.Field(column_name='parent', attribute='parent', widget=ForeignKeyWidget(Category, 'title'))

    class Meta: 
        model = Category 
 
        
class CategoryAdmin(ImportExportActionModelAdmin): 
    resource_class = GenerateUrlChPU 
    list_display = [field.name for field in Category._meta.fields if field.name != "id"]
    

class UslusgiResource(resources.ModelResource): 
    prepopulated_fields = {'slug': ('title',)}
    parent_category = fields.Field(column_name='parent_category', attribute='parent_category', widget=ForeignKeyWidget(Category, 'title'))
    
    class Meta: 
        model = Uslusgi 

        
class UslugiAdmin(ImportExportActionModelAdmin): 
    resource_class = UslusgiResource 
    list_display = [field.name for field in Uslusgi._meta.fields if field.name != "id"]


        
class MetaAdmin(ImportExportActionModelAdmin): 
    list_display = [field.name for field in Meta._meta.fields if field.name != "id"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Uslusgi, UslugiAdmin ) 
admin.site.register(Meta, MetaAdmin)
