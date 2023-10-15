from django.urls import path
from catalog.views import contacts,home, catalog
urlpatterns =[
    path('',home),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog, name='catalog')

]