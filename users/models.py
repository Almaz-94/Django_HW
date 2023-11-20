from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'null':True, 'blank':True}
class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="почта", unique=True)
    phone = models.CharField(max_length=30, verbose_name="телефон",**NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар',**NULLABLE)
    country = models.CharField(max_length=100,verbose_name="страна",**NULLABLE)
    verified = models.BooleanField(verbose_name='активирован', default=False)
    verification_code = models.CharField(max_length=50, verbose_name="код активации", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


