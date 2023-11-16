from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import render
from django.core.mail import send_mail
from newsletter.models import Newsletter


def success(request):
    email = request.POST.get('email', '')
    data = ""
    send_mail('Welcome!', data, 'almav@yandex.ru',
              [email], fail_silently=False)

    return render(request, 'newsletter/success.html')

def start():
    # send_mail(self.letter, self.letter, 'almav@yandex.ru',
    #           [self.client], fail_silently=False)
    scheduler = BackgroundScheduler()
    scheduler.add_job(Newsletter().send_mail_periodically, 'interval', seconds=1)
    # scheduler.add_job(update_something, 'interval', seconds=1)
    scheduler.start()
