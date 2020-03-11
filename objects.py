# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:18:47 2020

@author: Leopold
"""
import math
import datetime
import random as rd

temps_init_emition = 25

class Dommaine_colision():
    def __init__(self, fin_de_sim):
        self.time = 0
        self.machines = []
        self.next_events = []
        self.past_events = []
        self.etat = D_LIBRE
    
    def ajout_machine(self, machine):
        self.machines.append(machine)
    
    def ajout_event(self, event):
        self.next_events.append(event)
        self.next_events.sort()
    
    def __repr__(self):
        return """Dommaine de colision au temps {}, avec :
            -{} machines 
            -{} evenements à venir
            -{} evenement passés
            """.format(self.time, len(self.machines), len(self.next_events ), len(self.past_events))

class Machine():
    """
    representation d'une machine connecté au reseau
    """
    def __init__(self, dommaine, loi):
        """
        initialise une nouvelle machine dans le dommaine de colision
        """
        self.dommaine = dommaine
        self.events = []
        self.loi = loi
        self.etat = M_INACTIF
        self.nombre_echec = 0
    
    def ajout_event(self, event):
        self.events.append(event)
        self.events.sort()
        self.dommaine.ajout_event(event)

    def attendre(self):
        dt = self.loi(self.nombre_echec)
        
        
class Etat_dommaine():
    """
    etat de la liaison
    
    f - libre
    r - risque de colition
    c - colision
    o - occupee
    """
    def __init__(self, type):
        """
        initinalise un objet representant l'état de la liaison
        """
        if type in ('f', 'r', 'c', 'o'):
            self.type = type
        else:
            raise ValueError
    def __eq__(self, autre):
        return self.type == autre.type

class Etat_machine():
    """
    i - rien
    d - debut de transmition
    e - emition
    a - attente suite a une colision
    """
    def __init__(self, type):
        """
        initinalise un objet representant l'état d'une machine
        """
        if type in ('i', 'd', 'e', 'a'):
            self.type = type
        else:
            raise ValueError
    def __eq__(self, autre):
        return self.type == autre.type
    
class Event():
    """
    representation des evenements simulés
    """
    def __init__(self, time, machine):
        self.time = time
        machine.ajout_event(self)

    def __ge__(self, autre):
        return self.time >= autre.time

    def __gt__(self, autre):
        return self.time > autre.time

class Loi():
    """
    represente un generateur de nombre aléatoire
    """
    def __init__(self, generateur):
        """
        initialise une loi de generation de nombre aleatoire

        Parameters
        ----------
        generateur : callable 
            la fonction ne doit prendre que une seul varriable, n, le nombre 
            d'échecs.
        """
        self.generateur = generateur
        
    def __call__(self, n):
        
        X = self.generateur(n)
        if X < 0:
            X = 0
        return int(round(X))

class Event_debut_emition(Event):
    def __init__(self, a ):
        pass












D_LIBRE = Etat_dommaine('f')
D_RISQUE = Etat_dommaine('r')
D_COLISION = Etat_dommaine('c')
D_OCCUPE = Etat_dommaine('o')

M_INACTIF = Etat_machine('i')
M_DEBUT = Etat_machine('d')
M_EMITION = Etat_machine('e')
M_ATTENNTE = Etat_machine('a')

DOM = Dommaine_colision(1000)