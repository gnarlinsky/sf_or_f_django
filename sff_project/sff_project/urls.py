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
    # TODO: book_id should not be optional
    #   http://www.webforefront.com/django/accessurlparamsviewmethods.html
    url(r'^vote_sf/(?P<book_id>\d+)/$', rateBooks_application.views.vote_sf),
    url(r'^vote_f/(?P<book_id>\d+)/$', rateBooks_application.views.vote_f),
)

urlpatterns += staticfiles_urlpatterns()
