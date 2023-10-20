from django.db import models
from django.utils import timezone

# Create your models here.

NULLABLE = {'blank':True,'null':True}

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание категории')
    # created_at = models.DateField(**NULLABLE)

    def __str__(self):
        return f'Category {self.name}'

    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id','name')

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/',verbose_name='Превью',**NULLABLE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True,**NULLABLE)
    last_change_date = models.DateField(auto_now=True,**NULLABLE)

    def __str__(self):
        return f'Product {self.name} in {self.category}'

    class Meta:
        verbose_name= 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id','name')

