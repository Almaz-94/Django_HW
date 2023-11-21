import random

from django.core.cache import cache
from django.conf import settings

from blog.models import BlogPost
from catalog.models import Category


def get_category_list():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
        else:
            category_list = Category.objects.all()
        return category_list


def get_random_blogposts(num):
    count = BlogPost.objects.count()
    if count < num:
        return random.sample(list(BlogPost.objects.all()), k=count)
    else:
        return random.sample(list(BlogPost.objects.all()), k=num)