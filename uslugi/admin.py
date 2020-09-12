from django.contrib import admin
from .models import Category
from .models import Uslusgi

class GenerateUrlChPU(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, GenerateUrlChPU)
admin.site.register(Uslusgi, GenerateUrlChPU ) 
