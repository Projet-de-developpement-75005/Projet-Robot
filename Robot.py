import math
import pygame

# Couleurs
ROUGE = (200, 0, 0)
BLEU = (0, 0, 200)

# Paramètres du robot
ROBOT_LONGUEUR = 60
ROBOT_LARGEUR = 30

class Robot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angle = 0  # Orientation du robot
        self.vitesse_roue_gauche = 0
        self.vitesse_roue_droite = 0

    


    def afficher_position(self):
        print(f"Position actuelle : ({self.x}, {self.y}), Orientation : {self.orientation}°")

   
    def tourner(self, angle):
        """Tourne le robot d'un certain angle (en degrés)"""
        self.orientation = (self.orientation + angle) % 360
        print(f"Orientation actuelle : {self.orientation}°")
        
    