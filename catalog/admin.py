from django.contrib import admin
from catalog.models import Product,Category, Version

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date','last_change_date')
    list_display = ('pk','name','price','category','creation_date','last_change_date')
    list_filter = ('category',)
    search_fields = ('name','description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','name')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'version_number','version_name','is_current','product')