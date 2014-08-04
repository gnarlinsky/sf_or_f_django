from django import template
from django.contrib.auth.models import User
from rateBooks_application.models import Book, Vote

register = template.Library()

@register.filter
def user_voted_for_book(user_id, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=user_id)
    return Vote.user_voted_for_book(user=user, book=book)

@register.filter
def user_voted_sf_for_book(user_id, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=user_id)
    return Vote.user_voted_sf_for_book(user, book)

@register.filter
def user_voted_f_for_book(user_id, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=user_id)
    return Vote.user_voted_f_for_book(user, book)
