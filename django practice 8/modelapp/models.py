from django.db import models


class BookManager(models.Manager):
    def sort_by_rate(self):
         query = self.order_by('-rate')
         return query


class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    free = models.BooleanField(default=True)

    objects = BookManager()

    def __str__(self):
        return self.name
