from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rateBooks_application.models import Book, Vote

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

@login_required
def vote_sf(request, book_id):
    """ Retrieve the book with this id and increment its votes """
    #book = Book.objects.get(id=book_id)
    #book.votes_sf += 1
    #book.save()

    # Get the logged-in user and associate with this vote
    # If this vote exists (if user has already voted for this book), change the
    # existing vote. Otherwise, create a new one.
    user = request.user
    book = Book.objects.get(id=book_id)
    # TODO: best practices on how to get the actual User object from the
    #   queryset (indexing? something else?)
    try:
        vote = Vote.objects.get(book=book, user=user)
    except Vote.DoesNotExist:
        vote = Vote.objects.create(book=book, user=user)
    vote.vote = Vote.SCIENCE_FICTION
    vote.save()

    return HttpResponseRedirect('/')

@login_required
def vote_f(request, book_id):
    """ Retrieve the book with this id and increment its votes """
    #book = Book.objects.get(id=book_id)
    #book.votes_f += 1
    #book.save()

    # TODO: so would it be better to just have votes in the Votes model and add
    # them up for each book? I.e. above you would actuall not do book.votes_f,
    # do blah.get_votesblah.  So take care of the above....

    # No! you'd have to do more complicated stuff in order to have book.votes_f,
    # etc. 

    # Get the logged-in user and associate with this vote
    # If this vote exists (if user has already voted for this book), change the
    # existing vote. Otherwise, create a new one.
    user = request.user
    book = Book.objects.get(id=book_id)
    try:
        vote = Vote.objects.get(book=book, user=user)
    except Vote.DoesNotExist:
        vote = Vote.objects.create(book=book, user=user)
    vote.vote = Vote.FANTASY
    vote.save()


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
