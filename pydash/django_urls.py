from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',lambda x:TemplateResponse(x,"pub/index.jade")),
    url(r'^dash$',lambda x:TemplateResponse(x,"dash/index.jade")),
    # url(r'^tweb/', include('tweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
