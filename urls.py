from django.urls import path
from .views import liste_patients, ajouter_patient , modifier_patient , supprimer_patient

urlpatterns = [
    path('', liste_patients, name='liste_patients'),
    path('ajouter/', ajouter_patient, name='ajouter_patient'),
    path('modifier/<int:id>/', modifier_patient, name='modifier_patient'),
    path('supprimer/<int:id>/', supprimer_patient, name='supprimer_patient'),
]