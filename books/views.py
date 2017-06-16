from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Author, Book

class AuthorView(generic.ListView):
    model = Author
    template_name = 'books/author.html'

class BookView(generic.DetailView):
    model = Book
    template_name = 'books/book.html'