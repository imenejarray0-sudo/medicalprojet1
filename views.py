from django.shortcuts import render, redirect
from .models import RendezVous
from patients.models import Patient
from medecins.models import Medecin
from django.contrib.auth.decorators import login_required
# Liste des rendez-vous
@login_required
def liste_rendezvous(request):
    rendezvous = RendezVous.objects.all()
    return render(request, 'rendezvous/liste.html',
                  {'rendezvous': rendezvous})


# Ajouter rendez-vous
@login_required
def ajouter_rendezvous(request):

    patients = Patient.objects.all()
    medecins = Medecin.objects.all()

    if request.method == "POST":

        patient = request.POST['patient']
        medecin = request.POST['medecin']
        date = request.POST['date']
        heure = request.POST['heure']
        motif = request.POST['motif']


        RendezVous.objects.create(
            patient_id=patient,
            medecin_id=medecin,
            date=date,
            heure=heure,
            motif=motif
        )

        return redirect('liste_rendezvous')


    return render(request, 'rendezvous/ajouter.html',
                  {
                    'patients': patients,
                    'medecins': medecins
                  })


# Modifier rendez-vous
@login_required
def modifier_rendezvous(request, id):

    rendezvous = RendezVous.objects.get(id=id)

    patients = Patient.objects.all()
    medecins = Medecin.objects.all()


    if request.method == "POST":

        rendezvous.patient_id = request.POST['patient']
        rendezvous.medecin_id = request.POST['medecin']
        rendezvous.date = request.POST['date']
        rendezvous.heure = request.POST['heure']
        rendezvous.motif = request.POST['motif']

        rendezvous.save()

        return redirect('liste_rendezvous')


    return render(request,
                  'rendezvous/modifier.html',
                  {
                    'rendezvous': rendezvous,
                    'patients': patients,
                    'medecins': medecins
                  })


# Supprimer rendez-vous
@login_required
def supprimer_rendezvous(request, id):

    rendezvous = RendezVous.objects.get(id=id)

    rendezvous.delete()

    return redirect('liste_rendezvous')