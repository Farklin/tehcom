from django.db import models


class Meta(models.Model): 
    slug = models.TextField(max_length=70, unique=True, verbose_name = 'url') 
    title = models.CharField(max_length=150, verbose_name = 'title')
    description = models.CharField(max_length=150, verbose_name = 'description')

class Category(models.Model):

    slug = models.SlugField(max_length=70, verbose_name = 'url')
    title = models.CharField(max_length=150, verbose_name = 'Название')
    h1 = models.CharField(max_length=150, verbose_name = 'Заголовок h1', blank=True, null=True)
    content = models.TextField(null=True, blank=True, verbose_name ='Описание', default=None)
    image = models.ImageField(verbose_name = 'Изображение', null = True, upload_to = 'images/', blank = 'null', default = 'images/no_photo/no_photo.png')
    published = models.BooleanField() 
    parent = models.ForeignKey('self', verbose_name="Родительская категория", on_delete = models.PROTECT, null = True, blank=True)
    sorting = models.IntegerField(max_length=1, verbose_name='Сортировка', default='1', null = True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
        
    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
        image_img.short_description = 'Картинка'
        image_img.allow_tags = True

class Uslusgi(models.Model):
    slug = models.SlugField(max_length=70, unique=True, verbose_name = 'url', null=True, blank=True )
    title = models.CharField(max_length=150, verbose_name = 'Название')
    h1 = models.CharField(max_length=150, verbose_name = 'Заголовок h1', blank=True, null=True)
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


class Article(models.Model): 
    slug = models.SlugField(max_length=70, unique=True, verbose_name = 'url', null=True, blank=True )
    title = models.CharField(max_length=150, verbose_name = 'Название')
    h1 = models.CharField(max_length=150, verbose_name = 'Заголовок h1', blank=True, null=True)
    content = models.TextField(null=True, blank=True, verbose_name ='Контент страницы', default=None)
    parent = models.ForeignKey('self', verbose_name="Основаная", on_delete = models.PROTECT, null = True, blank=True)
    published = models.BooleanField(verbose_name = 'Публикация', default='True') 

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class ApplicationForm(models.Model): 
    STATUS_APLICATION = (
        ('new', 'Новая заявка'),
        ('performer_lookup', 'Заявка взята в обработку'),
        ('cancelled', 'Заказ отменен'),
        ('delivered_finish', 'Заказ завершен'),
    )

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    comment = models.TextField(max_length=300, verbose_name='Комментарий')
    name =  models.CharField(max_length=30, verbose_name='Имя')
    status = models.CharField(max_length=30, choices=STATUS_APLICATION, default='new')

    def __str__(self):
        return str(self.date)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки' 