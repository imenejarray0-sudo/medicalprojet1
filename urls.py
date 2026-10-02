from django.urls import path
from .views import (
    liste_consultations,
    ajouter_consultation
)


urlpatterns = [

    path(
        '',
        liste_consultations,
        name='liste_consultations'
    ),


    path(
        'ajouter/',
        ajouter_consultation,
        name='ajouter_consultation'
    ),

]