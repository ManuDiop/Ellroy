from django.db import models

class Book(models.Model):
    titre = models.CharField(max_length=200)
    date_publication = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title