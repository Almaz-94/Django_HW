from django.urls import path

from catalog.views import contacts
from newsletter.apps import NewsletterConfig
from newsletter.views import NewsletterCreateView, NewsletterDeleteView, NewsletterDetailView, NewsletterListView, \
    NewsletterUpdateView, ManagerNewsletterUpdateView
# from django.conf.urls import url

app_name= NewsletterConfig.name

urlpatterns = [

    path('create/', NewsletterCreateView.as_view(), name='create'),
    path('', NewsletterListView.as_view(), name='list'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete'),
    path('read/<int:pk>/', NewsletterDetailView.as_view(), name='read'),
    path('manager_update_news/<int:pk>/', ManagerNewsletterUpdateView.as_view(), name='manager_update_news'),
]
