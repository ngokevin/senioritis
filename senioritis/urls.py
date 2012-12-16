from django.conf import settings
from django.conf.urls.defaults import include, patterns, url


urlpatterns = patterns('views',
    url(r'^$', 'home', name='home'),
)


if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))
