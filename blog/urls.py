from django.urls import path
from blog.views import BlogpostCreateView,BlogpostListView,BlogpostDetailView,BlogpostUpdateView,BlogpostDeleteView
from blog.apps import BlogConfig

app_name= BlogConfig.name

urlpatterns =[
    #path('',home, name='home'),
    path('create/', BlogpostCreateView.as_view(), name='create'),
    path('',BlogpostListView.as_view(), name='list'),
    path('post/<int:pk>/', BlogpostDetailView.as_view(), name='post'),
    path('update/<int:pk>/', BlogpostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogpostDeleteView.as_view(), name='delete'),

]