from django.db import models
from patients.models import Patient
from medecins.models import Medecin


class Consultation(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    medecin = models.ForeignKey(
        Medecin,
        on_delete=models.CASCADE
    )

    date = models.DateField()
    diagnostic = models.TextField()
    traitement = models.TextField()
    remarques = models.TextField(blank=True)

    def __str__(self):
        return f"Consultation {self.patient} - {self.date}"