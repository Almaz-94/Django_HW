from django.urls import path
from catalog.views import contacts, ProductListView,ProductDetailView
from catalog.apps import CatalogConfig

app_name= CatalogConfig.name

urlpatterns =[
    #path('',home, name='home'),
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    #path('product/<int:id>/', product, name='product')
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product')
]