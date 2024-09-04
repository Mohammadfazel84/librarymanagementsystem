from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('books/<int:book_id>', views.books,name='books'),
    path('add',views.add,name='add'),
    path('update/<int:book_id>',views.update,name='update'),
    path('delete/<int:book_id>',views.delete,name='delete'),
    path('search',views.search,name='search'),
    path('filter',views.filter,name='filter'),
]
