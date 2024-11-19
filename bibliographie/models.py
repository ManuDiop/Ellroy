from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    date_publication = models.IntegerField()
    genre = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    couverture = models.ImageField(upload_to='couvertures/', blank=True, null=True)  # Champ pour l'image de couverture
    synopsis = models.TextField(blank=True, null=True)  # Champ pour le synopsis

    def __str__(self):
        return self.titre
    
class Commentaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur} le {self.date.strftime('%d/%m/%Y à %H:%M')}"

