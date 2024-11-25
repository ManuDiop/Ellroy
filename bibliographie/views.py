from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Livre, Commentaire
from .forms import CommentaireForm



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
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

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

def detail_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    commentaires = Commentaire.objects.filter(livre=livre)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.utilisateur = request.user
            commentaire.livre = livre
            commentaire.save()
            return redirect('detail_livre', livre_id=livre_id)
    else:
        form = CommentaireForm()
    
    context = {
        'livre': livre,
        'commentaires': commentaires,
        'form': form,
    }

    return render(request, 'bibliographie/detail-livre.html', context)

@login_required
def delete_comment(request, commentaire_id):
    commentaire = get_object_or_404(Commentaire, pk=commentaire_id)
    if commentaire.utilisateur == request.user:
        commentaire.delete()
        messages.success(request, 'Vous avez supprimé le commentaire.')
    else:
        messages.error(request, 'Vous n\'êtes pas autorisé à supprimer ce commentaire.')

    return redirect('detail_livre', livre_id=commentaire.livre.id)