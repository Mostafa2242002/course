from django.shortcuts import render

# Create your views here.
def books(request):
    return render(request,'pages/books.html')