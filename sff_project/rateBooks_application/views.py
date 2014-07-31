from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from rateBooks_application.models import Book

# TODO: http://effectivedjango.com/tutorial/views.html,
#       see Class Based Views vs methods

# TODO: just guessing if this is an appropriate class for these two views
#class MyView(View):
#    def get(self, request, *args, **kwargs):
#        return HttpResponse("Hello, World")

# TODO:  so, should vote_f, vote_sf, actually fall under ListBookView?
# TOODO: yeah, return HttpResponseRedirect('/') really does seem sort of
# unsophisticated.  
#
# TODO: don't reload everything! Way more asynchronous....

def vote_sf(request, book_id):
   """ Retrieve the book with this id and increment its votes """
   book = Book.objects.get(id=book_id)
   book.votes_sf += 1
   book.save()
   return HttpResponseRedirect('/')

def vote_f(request, book_id):
   """ Retrieve the book with this id and increment its votes """
   book = Book.objects.get(id=book_id)
   book.votes_f += 1
   book.save()
   return HttpResponseRedirect('/')

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
