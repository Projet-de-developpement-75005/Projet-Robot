import pygame
import time
import math 
from robot import Voiture
from environnement import Environnement
from interface import Interface, VOITURE_LONGUEUR, VOITURE_LARGEUR


class EnvRobot:
    def _init_(self):
        pygame.init()
        self.largeur = 900
        self.hauteur = 800
        self.environnement = Environnement(self.largeur, self.hauteur)
        self.voiture = Voiture(self.largeur // 2, self.hauteur // 2)
        self.interface = Interface(self.largeur, self.hauteur)
        self.clock = pygame.time.Clock()
        self.running = True

        # Démarrer l'horloge
        self.temps_depart = time.time()

        # Demander à l'utilisateur s'il veut entrer manuellement les vitesses et la direction
        self.entrer_manuellement = input("Voulez-vous entrer manuellement les vitesses et la direction ? (o/n) : ").lower() == "o"

        if self.entrer_manuellement:
            # Entrer les vitesses des roues
            self.voiture.vitesse_roue_gauche = int(input("Entrez la vitesse de la roue gauche (-8 à 8) : "))
            self.voiture.vitesse_roue_droite = int(input("Entrez la vitesse de la roue droite (-8 à 8) : "))

            