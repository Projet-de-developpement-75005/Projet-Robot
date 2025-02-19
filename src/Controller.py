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

    def demander_controle_utilisateur(self):
        """Demande à l'utilisateur s'il souhaite entrer manuellement les vitesses des roues."""
        print("Voulez-vous entrer manuellement les vitesses des roues ? (o/n)")
        choix = input().lower()
        if choix == "o":
            self.robot.vitesse_roue_gauche = float(input("Entrez la vitesse de la roue gauche (-8 à 8) : "))
            self.robot.vitesse_roue_droite = float(input("Entrez la vitesse de la roue droite (-8 à 8) : "))
        else:
            print("Utilisez les touches du clavier pour contrôler la voiture.")
            self.activer_controle_clavier(self.environnement.interface.canvas)  # Activer le contrôle clavier
            
def vitesse_roues(self, left_speed, right_speed):
def deplacer_robot(self):
def verif_collision(self):
def _deplacer_trajectoire_carre(self):
def _gerer_deplacement_clavier(self):