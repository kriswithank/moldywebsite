from django import template
from django.http import HttpRequest


register = template.Library()


@register.simple_tag
def app_active(request, app_name):
    if app_name in request.resolver_match.app_names:
        return 'active'
    else:
        return ''
