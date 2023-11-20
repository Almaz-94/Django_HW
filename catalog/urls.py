from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductManagersUpdate, CategoryListView, main_page
from catalog.apps import CatalogConfig

app_name= CatalogConfig.name

urlpatterns =[
    path('', main_page, name='home'),
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', cache_page(120)(ProductDetailView.as_view()), name='product'),
    path('create', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('moderator_update/<int:pk>', ProductManagersUpdate.as_view(), name='moderator_update_product'),
    path('categories', CategoryListView.as_view(), name='categories'),
]