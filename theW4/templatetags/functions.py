from django import template
import re

register = template.Library()

@register.filter(name='stylelinks')
def stylelinks(text):
    return re.sub("<a ", "<a style=\"text-decoration: underline; color:#FF0000;\" ", text, flags=re.IGNORECASE)