from django import forms
from .models import Commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        labels = {
            'contenu': '',
        }
        widgets = {
            'contenu': forms.Textarea(attrs={'placeholder': 'Écrivez votre commentaire'}),
        }