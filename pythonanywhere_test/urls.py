from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pythonanywhere_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'panywhere.views.home', name='home'),
    url(r'^post/', 'panywhere.views.post', name='post'),

    url(r'^admin/', include(admin.site.urls)),
)
