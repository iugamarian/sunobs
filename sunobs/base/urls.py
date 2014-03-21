from django.conf.urls import patterns, url

urlpatterns = patterns(
    'sunobs.base.views',
    url(r'^$', 'index', name='index'),
    url(r'^logout/', 'logout_user', name='logout_user'),
    url(r'^me/', 'p_view', name='p_view'),
    url(r'^me/edit/', 'p_edit', name='p_edit'),
)
