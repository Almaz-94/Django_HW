from django.db import models


NULLABLE = {'blank':True,'null':True}
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Ссылка')
    text = models.TextField(verbose_name='Текст записи')
    image = models.ImageField(upload_to='blogpost/',verbose_name='Превью',**NULLABLE)
    creation_date = models.DateField(auto_now_add=True)
    published = models.BooleanField(verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'Blog post "{self.title}"\n{self.slug}\n'

    class Meta:
        verbose_name= 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ('id','title')
