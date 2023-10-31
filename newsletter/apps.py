from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'

    # def ready(self):
    #     from newsletter.models import Newsletter, NLLogs
    #     for obj in Newsletter.objects.all():
    #
    #         obj.send_mail_periodically()


