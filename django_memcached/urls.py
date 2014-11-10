try:
    from django.conf.urls.defaults import *
except ImportError:  # django >= 1.6
    from django.conf.urls import patterns


urlpatterns = patterns('',
    (r'^$', 'django_memcached.views.server_list'),
    (r'^(\d+)/$', 'django_memcached.views.server_status'),
)
