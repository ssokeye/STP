from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'membership.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
