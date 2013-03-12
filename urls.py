from django.conf.urls import patterns, include, url
from django.conf import settings
from django.shortcuts import HttpResponse

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sunobs.views',
    (r'^$', 'home'),
    (r'^logout/', 'logout_user'),
)

urlpatterns += patterns('sunobs.observations.views',
    (r'^dashboard/', 'dashboard'),
    (r'^o/(?P<id>\d+)/', 'o_view'),
    (r'^o/create/', 'o_edit'),
    (r'^o/(?P<id>\d+)/edit/', 'o_edit'),
)

urlpatterns += patterns('sunobs.profiles.views',
    (r'^register/', 'register'),
    (r'^me/', 'p_view'),
    (r'^me/edit/', 'p_edit'),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^browserid/', include('django_browserid.urls')),

    #generate a robots.txt
    (r'^robots\.txt$',
        lambda r: HttpResponse(
            "User-agent: *\n%s: /" % 'Disallow' if settings.DEBUG else 'Allow',
            mimetype="text/plain"
        )
    )
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^.*?media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
