from django.conf import settings
from django_hosts import patterns, host
#from shortener.hostsconf import urls as redirect_urls

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'shortener.hostsconf.urls', name='wildcard'),
)