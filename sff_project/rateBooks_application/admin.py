from django.contrib import admin
from rateBooks_application.models import Book


# TODO:
#   ugh, this is so awkward, using admin for everything!!!
class BookAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj = None):
        # nobody can edit votes
        self.readonly_fields = ('votes_sf', 'votes_f')
        if obj:
            if request.user.is_staff and not request.user.is_superuser:
                print '='*50
                self.readonly_fields = self.readonly_fields + ('title', 'author')
        return self.readonly_fields

    #readonly_fields = (
    #                    #'title', 'author',
    #                    'votes_sf', 'votes_f',
    #                  )

    fieldsets = [
        ( 'Book Info',  {'fields': ['title', 'author']    } ),
        ( 'Votes',      {'fields': ['votes_sf', 'votes_f']} ),
    ]

admin.site.register(Book, BookAdmin)


# TODO:
# http://stackoverflow.com/questions/5021928/django-admin-permissions-to-modify-models-attributes

# * Subclass AdminSite!
# http://www.tryolabs.com/Blog/2012/06/18/django-administration-interface-non-staff-users/
