from django.db import models

class Category(models.Model):

    slug = models.SlugField(max_length=70, unique=True, verbose_name = 'url')
    title = models.CharField(max_length=150, verbose_name = 'Название')
    content = models.TextField(null=True, blank=True, verbose_name ='Описание', default=None)
    image = models.ImageField(verbose_name = 'Изображение', null = True, upload_to = 'images/', blank = 'null')
    published = models.BooleanField() 

    sorting = models.IntegerField(max_length=1, verbose_name='Сортировка', default='1', null = True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Uslusgi(models.Model):
    slug = models.SlugField(max_length=70, unique=True, verbose_name = 'url', null=True, blank=True )
    title = models.CharField(max_length=150, verbose_name = 'Название')
    content = models.TextField(null=True, blank=True, verbose_name ='Описание', default=None)
    published = models.BooleanField(verbose_name = 'Публикация', default='False') 
    price = models.IntegerField(verbose_name = 'Цена', default='1')
    image = models.ImageField(verbose_name = 'Изображение', null = True, upload_to = 'images/' ) 

    parent_category = models.ForeignKey(Category, verbose_name='Главная категория', on_delete=models.PROTECT, null = True, blank=True)
    similar_services = models.ManyToManyField('self', verbose_name='Похожие услуги', null = True,  blank=True)
    sorting = models.IntegerField(max_length=1, verbose_name='Сортировка', default='1', null = True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

