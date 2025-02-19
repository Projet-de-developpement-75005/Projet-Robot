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

    def deplacement_carre(self):
        """Déplace le robot sur une trajectoire en carré tout en vérifiant les limites."""
        if self.cote_parcouru < self.cote_carre:
            # Avancer dans la direction actuelle
            self.robot.vitesse_roue_gauche = 5  # Vitesse de déplacement
            self.robot.vitesse_roue_droite = 5
            # Déplacer le robot avec les obstacles (s'ils existent)
            obstacles = self.environnement.obstacles if self.environnement else []
            self.robot.deplacer(obstacles)
            self.cote_parcouru += 1
        else:
            # Après avoir parcouru un côté, tourner de 90°
            self.robot.angle += 90
            self.cote_courant = (self.cote_courant % 4) + 1
            self.cote_parcouru = 0
            # Réinitialiser les vitesses pour le nouveau côté
            self.robot.vitesse_roue_gauche = 0
            self.robot.vitesse_roue_droite = 0

        def deplacement_manuel(self, vitesse_gauche, vitesse_droite):
            """Permet de contrôler le robot manuellement."""
            self.robot.vitesse_roue_gauche = vitesse_gauche
            self.robot.vitesse_roue_droite = vitesse_droite

        def arreter_robot(self):
            """Arrête le robot."""
            self.robot.stop()
def vitesse_roues(self, left_speed, right_speed):
def deplacer_robot(self):
def verif_collision(self):
