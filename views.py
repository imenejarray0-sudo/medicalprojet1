from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from medecins.models import Medecin
from rendezvous.models import RendezVous
from consultations.models import Consultation
@login_required
def home(request):
    nombre_patients = Patient.objects.count()

    nombre_medecins = Medecin.objects.count()

    nombre_rendezvous = RendezVous.objects.count()

    nombre_consultations = Consultation.objects.count()


    return render(
        request,
        'home.html',
        {
            'patients': nombre_patients,
            'medecins': nombre_medecins,
            'rendezvous': nombre_rendezvous,
            'consultations': nombre_consultations,
        }
    )