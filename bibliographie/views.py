from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Livre


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Vous êtes connecté.')
            return redirect('homepage')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrects.')

    return render(request, 'bibliographie/login.html')

def signup_view(request):
    return render(request, 'bibliographie/signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté.')
    return redirect('homepage')

def homepage(request):
    livres = Livre.objects.all()
    return render(request, 'bibliographie/homepage.html', {'livres': livres})