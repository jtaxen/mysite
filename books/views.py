from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Author, Book

class AuthorListView(generic.ListView):
    """Shows a list of all authors"""
    template_name = 'books/authorlist.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.all().order_by('surname')

class AuthorView(generic.DetailView):
    """Shows the works of one author"""
    model = Author
    template_name = 'books/author.html'

class BookView(generic.DetailView):
    """Shows details of one book"""
    model = Book
    template_name = 'books/book.html'