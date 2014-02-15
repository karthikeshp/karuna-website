from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # URL For Media
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('dkapp.views',
    url(r'^$', 'home', name='home'),
    url(r'^events/$', 'events', name='events'),
    url(r'^gallery/$', 'gallery', name='gallery'),
)