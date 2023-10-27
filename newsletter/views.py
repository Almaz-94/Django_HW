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


# def index(request):
#     return render(request, 'newsletter/index.html')
#
#
# def success(request):
#     email = request.POST.get('email', '')
#     data = """
# Hello there!
#
# I wanted to personally write an email in order to welcome you to our platform.\
#  We have worked day and night to ensure that you get the best service. I hope \
# that you will continue to use our service. We send out a newsletter once a \
# week. Make sure that you read it. It is usually very informative.
#
# Cheers!
# ~ Yasoob
#     """
#     send_mail('Welcome!', data, 'almav@yandex.ru',
#               [email], fail_silently=False)
#
#     return render(request, 'newsletter/success.html')
# # send_mail('Django mail', 'This e-mail was sent with Django.',
# #               'almazziapov@yandex.ru.com', ['almaz28-10@mail.ru'], fail_silently=False)