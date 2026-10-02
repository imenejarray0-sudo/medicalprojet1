from django.shortcuts import render, redirect
from .models import Consultation
from patients.models import Patient
from medecins.models import Medecin
from rendezvous.models import RendezVous
from django.contrib.auth.decorators import login_required
@login_required
def liste_consultations(request):

    consultations = Consultation.objects.all()

    return render(
        request,
        'consultations/liste.html',
        {'consultations': consultations}
    )


@login_required
def ajouter_consultation(request):

    patients = Patient.objects.all()
    medecins = Medecin.objects.all()
    rendezvous = RendezVous.objects.all()


    if request.method == "POST":

        Consultation.objects.create(

            patient_id=request.POST['patient'],
            medecin_id=request.POST['medecin'],
            rendezvous_id=request.POST['rendezvous'],
            date=request.POST['date'],
            diagnostic=request.POST['diagnostic'],
            traitement=request.POST['traitement']

        )

        return redirect('liste_consultations')


    return render(
        request,
        'consultations/ajouter.html',
        {
            'patients':patients,
            'medecins':medecins,
            'rendezvous':rendezvous
        }
    )
