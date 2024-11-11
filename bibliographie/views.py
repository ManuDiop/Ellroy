from django.shortcuts import render
from .models import Livre

def homepage(request):
    livres = Livre.objects.all()
    return render(request, 'bibliographie/homepage.html', {'livres': livres})

def login(request):
    return render(request, 'bibliographie/login.html')

def signup(request):
    return render(request, 'bibliographie/signup.html')