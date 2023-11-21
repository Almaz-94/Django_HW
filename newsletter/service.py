from django.conf import settings
from django.core.cache import cache

from newsletter.models import Client


def is_member(user,group_name):
    return user.groups.filter(name=group_name).exists()


def get_cached_clients_list():
    if settings.CACHE_ENABLED:
        key = 'client_list'
        client_list = cache.get(key)
        if client_list is None:
            client_list = Client.objects.all()
            cache.set(key, client_list)
        else:
            client_list = Client.objects.all()
        return client_list




