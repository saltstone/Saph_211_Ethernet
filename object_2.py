# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:43:09 2020

@author: Leopold
"""

class Domaine():
    def __init__(self):
        self.time = 0
        self.machines = []
        self.events = []
        #self.etat = Etat_D_Libre
    
    def __repr__(self):
        C = """Domaine à t={} dans l'etat {}, avec:
    - {} machines, 
    - {} evenement"""
        return C.format(self.time, len(self.machines), len(self.events))

    def visiblement_libre(self):
        return self.etat.visiblement_libre
    
    def changement_etat(self, cible):
        self.etat.end(self)
        cible.begin(self)
        self.etat = cible
        
class Etat():
    def run(self):
        assert 0, "not implement"
    
    def next(self, commande):
        assert 0, "not implement"

class Etat_Domaine(Etat):
    def check_type(self, cible):
        return isinstance(self, Domaine)

class Etat_D_Libre(Etat_Domaine):
    def __init__(self, domaine):
        self.domaine = domaine
        
class Etat_D_Risque(Etat_Domaine):
    
class Etat_D_Occupe(Etat_Domaine):

class Etat_D_Collison(Etat_Domaine):

DOMAINE = Domaine()