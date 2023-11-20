from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'

    def ready(self):
        from newsletter.models import Newsletter
        for obj in Newsletter.objects.all():
            if obj.is_active:
                obj.send_mail_periodically()


