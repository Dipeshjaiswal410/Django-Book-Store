from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from .models import Book

def index(request):
    books= Book.objects
    return render(request, 'index.html', {'books': books})

def aboutus(request):
    return render(request, 'about.html')

