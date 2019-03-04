from django import template

register = template.Library()

@register.filter(name='cuttag')
def cuttag(value, arg):
    """
        this cuts out all values of "arg" from string
    """
    return value.replace(arg, '')

# register.filter('cuttag', cuttag)
