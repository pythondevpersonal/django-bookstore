from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = { "name" : "Murugan"}
    return render(request, 'books/index.html', context)

def home_page(request):
    return render(request, 'home_page.html')