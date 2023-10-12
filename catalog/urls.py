from django.urls import path
from catalog.views import contacts,home
urlpatterns =[
    path('',home),
    path('contacts/',contacts),

]