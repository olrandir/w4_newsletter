from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theW4.views.home', name='home'),
    # url(r'^theW4/', include('theW4.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', direct_to_template, {'template': 'index.html'}, name="home"),
#    url(r'^[^0-9]+$', redirect_to, {'url': '/'}),

	url(r'^list$','theW4.views.list', name='list'),
)
