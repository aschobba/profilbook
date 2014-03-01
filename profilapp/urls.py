from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'profilapp.views.home', name='home'),
    # url(r'^profilapp/', include('profilapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', auth_views.login,
    {'template_name': 'registration/login.html'},
    name='auth_login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addressbook/', include('addressbook.urls')),
    (r'^accounts/', include('registration.backends.default.urls')), 

)

urlpatterns += staticfiles_urlpatterns()
