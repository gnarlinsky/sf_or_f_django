from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from rateBooks_application.models import Book

# TODO: http://effectivedjango.com/tutorial/views.html, 
#       see Class Based Views vs methods

class ListBookView(ListView):
    """ List all Books in the database. """

    model = Book
    template_name = 'book_list.html'


class CreateBookView(CreateView):
    """ Form to create a new Book. """

    model = Book
    template_name = 'edit_book.html'   # TODO: edit or create?

    def get_success_url(self):
        """ When the form is successfully submitted, redirect user to list of
            all books. """
        return reverse('books-list')


#class BooksView(View):
#    """ Show info for books """

#    def get(self, request, *args, **kwargs):
#        """ Handle GET requests """
#        return HttpResponse("Hello, World")

#from django.shortcuts import render
# above was in original, but now following
# http://effectivedjango.com/tutorial/views.html
