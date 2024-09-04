from django import forms
from django.forms import ModelForm
from. models import Book

#Create form
class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name','writer','page_count','price','publish_date',)
    