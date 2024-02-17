from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def home_page(request):
    if request.method=='POST':
        book_info=BookForm(request.POST,request.FILES)
        if book_info.is_valid():
            book_info.save()  
        category_info=categoryform(request.POST)
        if category_info.is_valid():
            category_info.save()
    context={
        'form':BookForm(),
        'categories':Category.objects.all(),
        'book':Book.objects.all(),
        'category':len(Book.objects.all()),
        'cat':categoryform(),
        # "sold":Book.objects.filter(status="sold"),
        'roob':Book.objects.count(),
        'booksold':Book.objects.filter(status="sold").count(),
        'bookrental':Book.objects.filter(status="rental").count(),
        'bookavailable':Book.objects.filter(status="available").count(),
    }
    return render(request,'pages/index.html',context)
def books(request):
    search=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title= request.GET["search_name"]
        if title:
            search = search.filter(book_name__icontains=title)

    data=BookForm(request.POST)
    if data.is_valid():
         data.save()
    context={
        'cat':categoryform(),
        'categories':Category.objects.all(),
        'books':search,
        }
    return render(request,'pages/books.html',context)
def update(request,id):
    book_id=Book.objects.get(id=id)
    if request.method=="POST":
        book_save= BookForm(request.POST,request.FILES,instance=book_id)
        if  book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save=BookForm(instance=book_id)
    context={
        "book":book_save,
    }
    return render(request,'pages/update.html',context)
def delete_book(request,id):
    book_id=get_object_or_404(Book,id=id)
    if request.method=="POST":
        book_id.delete()
        return redirect('/')
    return render(request,'pages/delete.html')