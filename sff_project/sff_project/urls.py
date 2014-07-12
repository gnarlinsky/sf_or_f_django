from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import rateBooks_application.views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sff_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^new/',
        rateBooks_application.views.CreateBookView.as_view(),
        name='books-new',),
    url(r'^$',
        rateBooks_application.views.ListBookView.as_view(),
        name='books-list',),
)

urlpatterns += staticfiles_urlpatterns()
