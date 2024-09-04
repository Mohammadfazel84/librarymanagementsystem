from django.shortcuts import render, redirect
from .models import Book
from .forms import AddBookForm
from django.http import Http404, HttpResponseRedirect
# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,'index.html',context)

def books(request, book_id):
    if request.method == 'GET':

        book = Book.objects.get(pk = book_id)
        if book is not None:
            return render(request, 'books.html', {'book':book})
        else:
            raise Http404

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books = Book.objects.filter(name = searched)
        return render(request, 'search.html',{'searched':searched,'books':books})#
    else:
        return render(request, 'search.html',{})

def filter(request):
    submitted = False
    if request.method == 'GET':
        if 'submitted' in request.GET:
            submitted=True
        form = AddBookForm
        return render(request, 'filter.html',{'form':form,'submitted':submitted})
    else:
        form = AddBookForm(request.POST)
        books = Book.objects.filter(form)
        return render(request, 'filter.html',{'form':form,'books':books,'submitted':submitted})


def add(request):
    submitted = False
    if request.method =='POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add?submitted=true')

    elif request.method == 'GET':
        form = AddBookForm
        if 'submitted' in request.GET:
            submitted=True
    
    return render(request, 'add.html', {'form':form,'submitted':submitted})

def update(request, book_id):
    book = Book.objects.get(pk = book_id)
    form = AddBookForm(request.POST or None,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'update.html', {'book':book,'form':form})

def delete(request,book_id):
    book = Book.objects.get(pk = book_id)
    book.delete()
    return redirect('/')
