from django.shortcuts import render
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from catalog.forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

# def product(request, id):
#     product_obj = Product.objects.get(pk=id)
#     context = {
#         'object' : product_obj,
#         'title' : product_obj.name
#     }
#     return render(request,'catalog/product.html', context)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')