from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from catalog.forms import ProductForm, ProductFormManagers
from catalog.services import get_category_list


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/home.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, '\n', message)
    context = {
        'title': 'Contacts'
    }
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    # permission_required = 'catalog.add_product'
    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and not self.request.user.has_perm('catalog.delete_product'):
            raise Http404
        return self.object


class ProductManagersUpdate(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductFormManagers
    permission_required = 'catalog.change_product'

    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        return self.request.user.is_staff


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'catalog/category_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['categories'] = get_category_list()
        return context_data

