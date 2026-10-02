from django.shortcuts import render, redirect
from .models import Patient
from django.contrib.auth.decorators import login_required
@login_required
def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/liste.html', {'patients': patients})

@login_required
def ajouter_patient(request):
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        adresse = request.POST['adresse']

        Patient.objects.create(
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            adresse=adresse
        )

        return redirect('liste_patients')

    return render(request, 'patients/ajouter.html')
@login_required
def modifier_patient(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == "POST":
        patient.nom = request.POST['nom']
        patient.prenom = request.POST['prenom']
        patient.telephone = request.POST['telephone']
        patient.adresse = request.POST['adresse']

        patient.save()

        return redirect('liste_patients')

    return render(request, 'patients/modifier.html', {'patient': patient})
@login_required
def supprimer_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()

    return redirect('liste_patients')