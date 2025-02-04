import pygame
import time
import math 
from Robot import Robot
from Environment import Environment
from Interface import Interface, VOITURE_LONGUEUR, VOITURE_LARGEUR


class EnvRobot:
    def __init__(self):
        pygame.init()
        self.largeur = 900
        self.hauteur = 800
        self.environnement = Environment(self.largeur, self.hauteur)
        self.robot = Robot(self.largeur // 2, self.hauteur // 2)
        self.interface = Interface(self.largeur, self.hauteur)
        self.clock = pygame.time.Clock()
        self.running = True

        # Démarrer l'horloge
        self.temps_depart = time.time()

        # Demander à l'utilisateur s'il veut entrer manuellement les vitesses et la direction
        self.entrer_manuellement = input("Voulez-vous entrer manuellement les vitesses et la direction ? (o/n) : ").lower() == "o"

        if self.entrer_manuellement:
            # Entrer les vitesses des roues
            self.robot.vitesse_roue_gauche = int(input("Entrez la vitesse de la roue gauche (-8 à 8) : "))
            self.robot.vitesse_roue_droite = int(input("Entrez la vitesse de la roue droite (-8 à 8) : "))

            # Entrer la direction
            direction = input("Entrez la direction (haut, bas, gauche, droite) : ").lower()
            if direction == "haut":
                self.robot.angle = 90
            elif direction == "bas":
                self.robot.angle = 270
            elif direction == "gauche":
                self.robot.angle = 180
            elif direction == "droite":
                self.robot.angle = 0
            else:
                print("Direction non reconnue. Utilisation de la direction par défaut (haut).")
                self.robot.angle = 90

    def gerer_evenements(self):
        """Gère les événements du clavier."""
        if not self.entrer_manuellement:
            keys = pygame.key.get_pressed()

            # Réinitialiser les vitesses des roues
            self.robot.vitesse_roue_gauche = 0
            self.robot.vitesse_roue_droite = 0

            # Contrôle des vitesses des roues
            if keys[pygame.K_UP]:  # Avancer
                self.robot.vitesse_roue_gauche = 8
                self.robot.vitesse_roue_droite = 8

            if keys[pygame.K_DOWN]:  # Reculer
                self.robot.vitesse_roue_gauche = -8
                self.robot.vitesse_roue_droite = -8

            if keys[pygame.K_LEFT]:  # Tourner à gauche
                self.robot.vitesse_roue_gauche = -8
                self.robot.vitesse_roue_droite = 8

            if keys[pygame.K_RIGHT]:  # Tourner à droite
                self.robot.vitesse_roue_gauche = 8
                self.robot.vitesse_roue_droite = -8

    def run(self):
        """Boucle principale de la simulation."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if not self.entrer_manuellement:
                self.gerer_evenements()

            # Déplacer le robot en vérifiant les collisions
            self.robot.deplacer(self.environnement.obstacles, VOITURE_LONGUEUR, VOITURE_LARGEUR)
            self.robot.limiter_position(self.largeur, self.hauteur, VOITURE_LONGUEUR, VOITURE_LARGEUR)

            # Calculer le temps écoulé
            temps_ecoule = time.time() - self.temps_depart

            # Rafraîchir l'interface avec le temps écoulé
            self.interface.rafraichir_ecran(self.robot, self.environnement.obstacles, temps_ecoule)
            self.clock.tick(30)

        pygame.quit()

