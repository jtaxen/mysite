from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import TableViewCell

class TableView(generic.ListView):

    model = TableViewCell
    template_name = 'table/table.html'
    context_object_name = 'cell'

    def get_queryset(self):
        return TableViewCell.objects.all().order_by('cell_name')

def unorder(request):
    tc = TableViewCell.objects.all().order_by('cell_row')
    
