from django.shortcuts import render, redirect
from django.db.models import Q
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

def is_valid_query(param):
    return param != '' and param is not None


def filter(request):
    qs = Book.objects.all()
    authororname_contains = request.GET.get('authororname_contains')
    id_e = request.GET.get('id_e')
    maprice = request.GET.get('maprice')
    miprice = request.GET.get('miprice')
    madate = request.GET.get('madate')
    midate = request.GET.get('midate')
    checked = request.GET.get('checked')
    
    if is_valid_query(authororname_contains):
        qs = qs.filter(Q(name__icontains = authororname_contains) | Q(writer__icontains = authororname_contains)).distinct()
    elif is_valid_query(id_e):
        qs = qs.filter(id = id_e )
    
    if is_valid_query(maprice):
        qs = qs.filter(price__lte=maprice)
    if is_valid_query(miprice):
        qs = qs.filter(price__gte=miprice)
    if is_valid_query(madate):
        qs = qs.filter(publish_date__lte=madate)
    if is_valid_query(midate):
        qs = qs.filter(publish_date__gte=midate)
    context = {
        'queryset' : qs
    }
    if checked=='on':
            qs.delete()
            return redirect('/')
    return render(request,'filter.html',context)

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
