from django.contrib import admin
from blog.models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date',)
    list_display = ('pk','title','text','creation_date','published','view_count')
    list_filter = ('published','view_count')
    search_fields = ('text','title')
