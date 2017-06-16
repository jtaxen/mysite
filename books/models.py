from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    born = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    published = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} by {1}".format(self.name, self.author)
