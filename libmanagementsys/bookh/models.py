from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=64)
    writer = models.CharField(max_length=64)
    page_count = models.IntegerField()
    price = models.IntegerField()
    publish_date = models.DateField()
    def __str__(self):
            return (f'{self.id}- {self.name} by {self.writer}')