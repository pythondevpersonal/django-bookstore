from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.

booksData = open('books.json').read()
data = json.loads(booksData)

def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)

def home_page(request):
    return render(request, 'home_page.html')


def show(request, id):
    singlebook = list()
    for book in data:
        if book['id']==id:
            singlebook = book
    context = {'book': singlebook}
    return render(request, 'books/show.html', context)