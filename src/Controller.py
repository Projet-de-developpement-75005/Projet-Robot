from Robot import Robot
import time
import math

class Controller:
    def __init__(self, robot, environnement=None):
        self.robot = robot
        self.environnement = environnement  # Ajout de l'environnement
        self.cote_parcouru = 0
        self.cote_carre = 100  # Nombre de pas pour parcourir un côté du carré
        self.cote_courant = 1  # Côté actuel du carré (1 à 4)

def vitesse_roues(self, left_speed, right_speed):
def deplacer_robot(self):
def verif_collision(self):
def _deplacer_trajectoire_carre(self):
def _gerer_deplacement_clavier(self):