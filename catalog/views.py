from django.shortcuts import render
from catalog.models import Product,Category
# Create your views here.

def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list' : product_list,
        'title' : 'Home page'
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone,'\n',message)
    context = {
        'title': 'Contacts'
    }
    return render(request, 'catalog/contacts.html', context)

def product(request, id):
    product_obj = Product.objects.get(pk=id)
    context = {
        'object' : product_obj,
        'title' : product_obj.name
    }
    return render(request,'catalog/product.html', context)