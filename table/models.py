import datetime
from django.db import models
from django.utils import timezone


class TableViewCell(models.Model):
    cell_name = models.CharField(max_length=100)
    cell_row = models.IntegerField()
    cell_column = models.IntegerField()

    def __str__(self):
        return '{0}: ({1}, {2})'.format(self.cell_name, self.cell_row, self.cell_column)

