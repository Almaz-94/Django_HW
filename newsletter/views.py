from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404, HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from newsletter.forms import NewsletterForm, ManagerNewsletterForm
from newsletter.models import Newsletter, Client
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


class ManagerNewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = ManagerNewsletterForm
    success_url = reverse_lazy('newsletter:list')


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
