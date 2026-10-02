from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    date_naissance = models.DateField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"Dr. {self.nom} - {self.specialite}"