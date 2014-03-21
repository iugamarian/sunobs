from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

urlpatterns = patterns(
    '',

    # base urls
    url(r'^', include('sunobs.base.urls')),

    # observations urls
    url(r'^', include('sunobs.observations.urls')),

    # misc
    url(r'^admin/', include(admin.site.urls)),
    url(r'^browserid/', include('django_browserid.urls')),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    static_url = settings.STATIC_URL.lstrip('/').rstrip('/')
    from django.views.generic import TemplateView
    urlpatterns += patterns(
        '',
        url(r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        url(r'^%s/(?P<path>.*)$' % static_url, 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        url(r'^500/$', TemplateView.as_view(template_name='500.html')),
        url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    )
