import tkinter as tk 
import time
from Environment import Environment
from Robot import Robot
from Interface import Interface

class EnvRobot:
    def __init__(self, largeur=900, hauteur=800):
        self.largeur = largeur
        self.hauteur = hauteur

        # Configuration de la fenêtre principale
        self.root = tk.Tk()
        self.root.title("Simulation Robot")
        self.canvas = tk.Canvas(self.root, width=self.largeur, height=self.hauteur, bg="white")
        self.canvas.pack()
        
        # Initialisation des composants
        self.environnement = Environment(self.largeur, self.hauteur)
        self.robot = Robot(self.largeur // 2, self.hauteur // 2)
        self.interface = Interface(self.canvas, self.largeur, self.hauteur)

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
