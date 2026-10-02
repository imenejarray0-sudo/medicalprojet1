from django.urls import path

from .views import (
    liste_medecins,
    ajouter_medecin,
    modifier_medecin,
    supprimer_medecin
)


urlpatterns = [

    path('', liste_medecins, name='liste_medecins'),

    path('ajouter/',
         ajouter_medecin,
         name='ajouter_medecin'),

    path('modifier/<int:id>/',
         modifier_medecin,
         name='modifier_medecin'),

    path('supprimer/<int:id>/',
         supprimer_medecin,
         name='supprimer_medecin'),

]