from django import template


register = template.Library()
@register.filter()
def mediapath(img):
    if img:
        return f'/media/{img}'
    return '#'