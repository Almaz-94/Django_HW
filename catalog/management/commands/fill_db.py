from django.core.management import BaseCommand
from catalog.models import Product,Category

class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name':'Frozen food','description':'frozen goods'},
            {'name': 'Dairy and Eggs', 'description': 'milk,cheese,eggs'},
            {'name': 'Oils and Sauces', 'description': 'everything for seasoning'}
        ]
        category_for_creation = [Category(**category) for category in category_list]
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_creation)
        product_list=[
            {'name':'Frozen karp', 'description':'super frozen fish','category':Category.objects.get(name='Frozen food'),'price':200},
            {'name': 'Domik v derevne', 'description': 'milk 2.5%', 'category': Category.objects.get(name='Dairy and Eggs'), 'price': 100},
            {'name': 'Maheev', 'description': 'Chili sauce', 'category': Category.objects.get(name='Oils and Sauces'), 'price': 200},
        ]
        product_for_creation = [Product(**product) for product in product_list]
        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_creation)