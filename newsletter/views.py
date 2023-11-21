from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from newsletter.forms import NewsletterForm, ManagerNewsletterForm, LetterForm, ClientForm
from newsletter.models import Newsletter, Client, Letter
from django.urls import reverse, reverse_lazy

from newsletter.service import is_member


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and \
                not is_member(self.request.user, 'managers') and \
                not self.request.user.is_staff:
            raise Http404
        return self.object


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter

    def get_queryset(self):
        queryset = super().get_queryset()
        if not is_member(self.request.user, 'managers') and not self.request.user.is_superuser:
            queryset = queryset.filter(creator=self.request.user)
        return queryset


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and not self.request.user.has_perm('newsletter.delete'):
            raise Http404
        return self.object


class ManagerNewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = ManagerNewsletterForm
    success_url = reverse_lazy('newsletter:list')


class LetterCreateView(LoginRequiredMixin, CreateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('newsletter:letter_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class LetterDetailView(LoginRequiredMixin, DetailView):
    model = Letter


class LetterUpdateView(LoginRequiredMixin, UpdateView):
    model = Letter
    form_class = LetterForm

    def get_success_url(self):
        return reverse('newsletter:letter', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class LetterDeleteView(LoginRequiredMixin, DeleteView):
    model = Letter
    success_url = reverse_lazy('newsletter:letter_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class LetterListView(LoginRequiredMixin, ListView):
    model = Letter


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    success_url = reverse_lazy('newsletter:client_list')
    form_class = ClientForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy('newsletter:client_list')
    form_class = ClientForm


class ClientListView(LoginRequiredMixin,ListView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('newsletter:client_list')
