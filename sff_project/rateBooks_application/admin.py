from django.contrib import admin
from rateBooks_application.models import Book

class BookAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj = None):
        """
        print '='*50
        print dir(request.user)
        print '='*50
        print request.user.get_all_permissions()
        print '='*50
        """
        # nobody can edit votes
        self.readonly_fields = ('votes_sf', 'votes_f')
        if obj:
            # TODO: if not special perm.... 
            #if request.user.has_perm(blah):
            if request.user.is_staff and not request.user.is_superuser:
                print '='*50
                self.readonly_fields = self.readonly_fields + ('title', 'author')
                #return ['featured',] + self.readonly_fields
            #return self.readonly_fields
        #else:
        #    return self.readonly_fields
        return self.readonly_fields

    # TODO: so, for a not-superuser (i.e. just regular users of the site),
    # title and author fields should NOT be editable.
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
