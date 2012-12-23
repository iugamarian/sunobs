from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sunoss.views.home', name='home'),
    url(r'^logout/', 'sunoss.views.logout_user', name='logout_user'),

    url(r'^profile/', 'sunoss.profile.views.profile', name='profile'),

    #admin
    url(r'^admin/', include(admin.site.urls)),

    #browserid
    (r'^browserid/', include('django_browserid.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^.*?media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
