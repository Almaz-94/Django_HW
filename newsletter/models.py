import smtplib

from apscheduler.schedulers.background import BackgroundScheduler
from django.db import models
from datetime import datetime, date
from django.conf import settings


from django.core.mail import send_mail

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО', **NULLABLE)
    email = models.EmailField(verbose_name='Почта', unique=True)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name='создатель',
                                on_delete=models.SET_NULL,
                                **NULLABLE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Letter(models.Model):
    head = models.CharField(max_length=300, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Текст письма')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name='создатель',
                                on_delete=models.SET_NULL,
                                **NULLABLE)

    def __str__(self):
        return f'Письмо с темой: "{self.head}"'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Newsletter(models.Model):
    start = models.DateField(verbose_name='начало')
    end = models.DateField(verbose_name='конец')
    period = models.PositiveSmallIntegerField(default=7, verbose_name='периодичность в днях')
    client = models.ManyToManyField(Client, verbose_name='Клиенты рассылки')  # , related_name='newsletter')
    # status = models.ForeignKey(NLStatus, on_delete=models.DO_NOTHING, verbose_name='Статус')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name='создатель',
                                on_delete=models.SET_NULL,
                                **NULLABLE)

    status = models.CharField(max_length=30, default='CRE', verbose_name='Статус', choices=[
        ('CRE', 'Создана'),
        ('ONG', "Запушена"),
        ('END', "Завершена")])
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, verbose_name='Письмо рассылки')
    is_active = models.BooleanField(default=False, verbose_name='Активна')

    def update_status(self):
        if self.start > date.today():
            self.status = 'CRE'
        elif self.end > date.today():
            self.status = 'ONG'
        else:
            self.status = 'END'
        self.save()

    def send_mail_periodically(self):
        def send():
            try:
                send_mail(self.letter.head, self.letter.body,
                          'skylanser28.10.94@gmail.com',
                          list(self.client.all()), fail_silently=False)
                status = 'Удачно'
                err_text = ''
            except smtplib.SMTPException as error:
                status = 'Ошибка'
                if 'authentication failed' in str(error):
                    err_text = 'Ошибка аутентификации'
                elif 'suspicion of SPAM' in str(error):
                    err_text = 'Письмо было отклонено: подозрение на спам'
                else:
                    err_text = error
            finally:
                NLLogs.objects.create(
                    last_try=datetime.today(),
                    status=status,
                    newsletter=self,
                    error_text=err_text
                )
        if self.is_active:
            scheduler = BackgroundScheduler()
            scheduler.add_job(send, 'interval', start_date=self.start, end_date=self.end,
                              days=self.period)  #seconds=30) #
            scheduler.start()

    def __str__(self):
        return f'Рассылка №{self.pk}, автор {self.creator}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class NLLogs(models.Model):
    last_try = models.DateTimeField(auto_now=True, **NULLABLE)
    # server_response = models.PositiveSmallIntegerField(verbose_name='Ответ сервера', **NULLABLE)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='Рассылка')
    error_text = models.TextField(verbose_name='текст ошибки', **NULLABLE)
    status = models.CharField(max_length=30, verbose_name='Статус', **NULLABLE)

    def __str__(self):
        return f'Рассылка №{self.newsletter.pk}, попытка от {self.last_try}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
