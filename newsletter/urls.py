from django.urls import path
from newsletter.apps import NewsletterConfig
from newsletter.views import NewsletterCreateView, NewsletterDeleteView, NewsletterDetailView, NewsletterListView, NewsletterUpdateView
# from django.conf.urls import url

app_name= NewsletterConfig.name

urlpatterns = [
    # path('index/', index, name='index'),
    # path('index/success/', success, name='success'),
    path('create/', NewsletterCreateView.as_view(), name='create'),
    path('', NewsletterListView.as_view(), name='list'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete'),
    path('read/<int:pk>/', NewsletterDetailView.as_view(), name='read'),
]
