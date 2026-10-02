from django.shortcuts import render, redirect
from .models import Medecin
from django.contrib.auth.decorators import login_required

# Liste des médecins
@login_required
def liste_medecins(request):
    medecins = Medecin.objects.all()
    return render(request, 'medecins/liste.html', {'medecins': medecins})


# Ajouter médecin
@login_required
def ajouter_medecin(request):
    if request.method == "POST":

        nom = request.POST['nom']
        prenom = request.POST['prenom']
        specialite = request.POST['specialite']
        telephone = request.POST['telephone']

        Medecin.objects.create(
            nom=nom,
            prenom=prenom,
            specialite=specialite,
            telephone=telephone
        )

        return redirect('liste_medecins')

    return render(request, 'medecins/ajouter.html')
# Modifier médecin
@login_required
def modifier_medecin(request, id):

    medecin = Medecin.objects.get(id=id)

    if request.method == "POST":

        medecin.nom = request.POST['nom']
        medecin.prenom = request.POST['prenom']
        medecin.specialite = request.POST['specialite']
        medecin.telephone = request.POST['telephone']

        medecin.save()

        return redirect('liste_medecins')


    return render(request, 'medecins/modifier.html',
                  {'medecin': medecin})
# Supprimer médecin
@login_required
def supprimer_medecin(request, id):

    medecin = Medecin.objects.get(id=id)

    medecin.delete()

    return redirect('liste_medecins')