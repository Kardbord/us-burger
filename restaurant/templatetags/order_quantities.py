from django import template

register = template.Library()


@register.filter(name='val')
def val(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return 0
