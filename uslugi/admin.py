from django.contrib import admin
from .models import Category
from .models import Uslusgi

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources 
from import_export import fields 
from import_export.widgets import ForeignKeyWidget

class GenerateUrlChPU(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class UslusgiResource(resources.ModelResource): 
    parent_category = fields.Field(column_name='parent_category', attribute='parent_category', widget=ForeignKeyWidget(Category, 'title'))
    
    class Meta: 
        model = Uslusgi 

        
class UslugiAdmin(ImportExportActionModelAdmin): 
    resource_class = UslusgiResource 
    list_display = [field.name for field in Uslusgi._meta.fields if field.name != "id"]


admin.site.register(Category, GenerateUrlChPU)
admin.site.register(Uslusgi, UslugiAdmin ) 
