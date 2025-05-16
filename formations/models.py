from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField(default=date.today)
    date_fin = models.DateField(default=date.today)
    duree_jours = models.IntegerField()
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)

class Stagiaire(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Inscription(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    stagiaire = models.ForeignKey(Stagiaire, on_delete=models.CASCADE)
    date_inscription = models.DateField(auto_now_add=True)
from django.db import models


class NoteFormation(models.Model):
    stagiaire = models.ForeignKey('Stagiaire', on_delete=models.CASCADE)
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE)
    note = models.IntegerField()  # ou FloatField si tu veux des notes comme 4.5

    class Meta:
        unique_together = ('stagiaire', 'formation')  # Un stagiaire ne peut noter une formation qu’une seule fois

    def __str__(self):
        return f"{self.stagiaire} - {self.formation} : {self.note}"

class NoteFormation(models.Model):
    stagiaire = models.ForeignKey('Stagiaire', on_delete=models.CASCADE)
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE)
    note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Note {self.note} - {self.stagiaire} pour {self.formation}"