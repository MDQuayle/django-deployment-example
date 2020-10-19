from django import template

register = template.Library()

# two ways to do this either use this decorator or the bottom way
@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut', cut)
