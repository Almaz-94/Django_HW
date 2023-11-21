from django.urls import path

from catalog.views import contacts
from newsletter.apps import NewsletterConfig
from newsletter.views import NewsletterCreateView, NewsletterDeleteView, NewsletterDetailView, NewsletterListView, \
    NewsletterUpdateView, ManagerNewsletterUpdateView, LetterCreateView, LetterUpdateView, LetterDetailView, \
    LetterListView, LetterDeleteView, ClientCreateView, ClientUpdateView, ClientListView, ClientDeleteView

# from django.conf.urls import url

app_name= NewsletterConfig.name

urlpatterns = [

    path('create/', NewsletterCreateView.as_view(), name='create'),
    path('', NewsletterListView.as_view(), name='list'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete'),
    path('read/<int:pk>/', NewsletterDetailView.as_view(), name='read'),
    path('manager_update_news/<int:pk>/', ManagerNewsletterUpdateView.as_view(), name='manager_update_news'),
    path('create_letter/', LetterCreateView.as_view(), name='create_letter'),
    path('letter/<int:pk>/', LetterDetailView.as_view(), name='letter'),
    path('letter_list/', LetterListView.as_view(), name='letter_list'),
    path('update_letter/<int:pk>/', LetterUpdateView.as_view(), name='update_letter'),
    path('delete_letter/<int:pk>/', LetterDeleteView.as_view(), name='delete_letter'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]
