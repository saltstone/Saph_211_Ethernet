# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:18:47 2020

@author: Leopold
"""
import math
import datetime

class Dommaine_colision():
    def __init__(self):
        self.time = 0
        self.machines = []
        self.next_events = []
        self.past_events = []
        self.etat = "f" 
    
    def ajout_machine(self, machine:Machine):
        self.machines.append(machine)
        self.next_events =(self.next_events + machine.events).sort()

class Machine():
    def __init__(self, dommaine:Dommaine_colision):
        
class Etat_dommaine():
    """
    etat de la liaison
    
    f - libre
    r - risque de colition
    c - colision
    o - occupee
    """
    def __init__(self, type):
        if type in ('f', 'r', 'c', 'o'):
            self.type = type
        else:
            raise ValueError
        
class Event():
    def __init__(self, time, machine:Machine):
        
D_LIBRE = Etat_dommaine('f')
D_RISQUE = Etat_dommaine('r')
D_COLISION = Etat_dommaine('c')
D_OCCUPE = Etat_dommaine('o')