from django.urls import path

from .views import (
    liste_rendezvous,
    ajouter_rendezvous,
    modifier_rendezvous,
    supprimer_rendezvous
)


urlpatterns = [

    path('', liste_rendezvous,
         name='liste_rendezvous'),

    path('ajouter/',
         ajouter_rendezvous,
         name='ajouter_rendezvous'),

    path('modifier/<int:id>/',
         modifier_rendezvous,
         name='modifier_rendezvous'),

    path('supprimer/<int:id>/',
         supprimer_rendezvous,
         name='supprimer_rendezvous'),

]