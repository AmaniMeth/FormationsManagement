from datetime import date
from django.db import models

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
