from django.contrib import admin
from rateBooks_application.models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'author', 'votes_sf', 'votes_f',)
    # TODO: so, for a not-superuser (i.e. just regular users of the site),
    # title and author fields should NOT be editable.
    fieldsets = [
        ( 'Book Info',  {'fields':          ['title', 'author']    } ),
        ( 'Votes',      {'fields': ['votes_sf', 'votes_f']} ),
    ]

admin.site.register(Book, BookAdmin)


# TODO:
# http://stackoverflow.com/questions/5021928/django-admin-permissions-to-modify-models-attributes
