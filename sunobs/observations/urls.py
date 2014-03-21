from django.conf.urls import patterns, url

urlpatterns = patterns('sunobs.observations.views',
    url(r'^dashboard/', 'dashboard'),
    url(r'^o/(?P<id>\d+)/', 'o_view'),
    url(r'^o/create/', 'o_edit'),
    url(r'^o/(?P<id>\d+)/edit/', 'o_edit'),
)