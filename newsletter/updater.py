from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import render
from django.core.mail import send_mail
from newsletter.models import Newsletter

def update_something():
    print("this function runs every 10 seconds")

# def start():
#     scheluler = BackgroundScheduler()
#     scheluler.add_job(update_something, 'interval', seconds=10)
#     scheluler.start()

def success(request):
    email = request.POST.get('email', '')
    data = """
Hello there!

I wanted to personally write an email in order to welcome you to our platform.\
 We have worked day and night to ensure that you get the best service. I hope \
that you will continue to use our service. We send out a newsletter once a \
week. Make sure that you read it. It is usually very informative.

Cheers!
~ Yasoob
    """
    send_mail('Welcome!', data, 'almav@yandex.ru',
              [email], fail_silently=False)

    return render(request, 'newsletter/success.html')
# send_mail('Django mail', 'This e-mail was sent with Django.',
#               'almazziapov@yandex.ru.com', ['almaz28-10@mail.ru'], fail_silently=False)


def start():
    # send_mail(self.letter, self.letter, 'almav@yandex.ru',
    #           [self.client], fail_silently=False)
    scheduler = BackgroundScheduler()
    scheduler.add_job(Newsletter().send_mail_periodically, 'interval', seconds=1)
    # scheduler.add_job(update_something, 'interval', seconds=1)
    scheduler.start()
