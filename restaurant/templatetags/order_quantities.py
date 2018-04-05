from django import template

register = template.Library()

@register.filter(name='val')
def val(dict, key):
    try:
        return dict[key]
    except KeyError:
        return 0