from django.views.generic import CreateView, DetailView, ListView, UpdateView,DeleteView
from newsletter.models import Newsletter
from django.urls import reverse, reverse_lazy

class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = ('start', 'end', 'period', 'client', 'letter', 'status')
    success_url = reverse_lazy('newsletter:list')

class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ('start', 'end', 'period', 'client', 'letter','status')
    success_url = reverse_lazy('newsletter:list')


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:list')
