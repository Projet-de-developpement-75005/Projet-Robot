import time
import math
import tkinter as tk
from threading import Thread
from Model.robot import Robot
from Model.arene import Arene
from Model.obstacle import Obstacle
from view.view_2d import View

# Dimensions de l'arène
ARENE_LARGEUR = 500
ARENE_HAUTEUR = 500

class Simulation:
    def __init__(self, use_graphics=True):
        # Création de l'arène et positionnement du robot au centre
        self.arene = Arene(ARENE_LARGEUR, ARENE_HAUTEUR)
        self.robot = Robot(
            x=ARENE_LARGEUR / 2,
            y=ARENE_HAUTEUR / 2,
            orientation=0,
            vitesse_gauche=0,
            vitesse_droite=0,
            diametre_roue=10,
            distance_roues=20
        )
        # Ajout d'obstacles
        obstacle1 = Obstacle(100, 100, 50, 50)
        obstacle2 = Obstacle(100, 200, 30, 60)
        self.arene.ajouter_obstacle(obstacle1)
        self.arene.ajouter_obstacle(obstacle2)
        self.arene.ajouter_robot(self.robot)
        # Initialisation des angles des roues pour l'animation (optionnel)
        self.robot.angle_roue_gauche = 0.0
        self.robot.angle_roue_droite = 0.0

        self.use_graphics = use_graphics
        # Gestion de la séquence pour dessiner le carré
        self.commands = None
        self.current_command_index = 0
        self.command_time_remaining = 0
        self.running = False
        # Liste des points de la trajectoire (pour tracer le trait vert)
        self.trace_points = []

        # Création de la vue si l'affichage graphique est activé
        self.view = None
        if self.use_graphics:
            self.view = View(self.arene)
            # Appuyer sur Entrée dans la fenêtre lancera la séquence
            self.view.bind("<Return>", self.demarrer_carre)
        
        # Lancement du thread d'affichage console (toujours actif)
        self.console_thread = Thread(target=self.afficher_console)
        self.console_thread.daemon = True
        self.console_thread.start()

    def demarrer_carre(self, event=None):
        """
        Définit la séquence de commandes pour que le robot "dessine" un carré.
        Chaque côté consiste en :
         - Une phase d'avance (50 pixels à 20 px/s)
         - Une phase de virage de 90° (calculé à partir d'une vitesse de base et d'un delta)
        """
        vitesse_base = 20  # Vitesse de déplacement en pixels par seconde
        avancer_duration = 50 / vitesse_base  # 50 pixels en 2.5 secondes
        delta = 10  # Valeur de décalage pour le virage
        # Durée pour tourner 90° :
        tourner_duration = (math.pi / 2) / ((2 * delta) / self.robot.distance_roues)
        
        self.commands = []
        for _ in range(4):
            self.commands.append({"type": "avancer", "vitesse": vitesse_base, "duration": avancer_duration})
            self.commands.append({"type": "tourner", "vitesse": vitesse_base, "delta": delta, "duration": tourner_duration})
        self.current_command_index = 0
        self.command_time_remaining = self.commands[0]["duration"]
        # Réinitialise le trace en gardant le point de départ
        self.trace_points = [(self.robot.x, self.robot.y)]

    def update_strategy(self, delta_t):
        """
        Applique la commande active pendant sa durée.
        Pour "avancer", les deux roues tournent à la même vitesse.
        Pour "tourner", on ajuste les vitesses différemment.
        Une fois la séquence terminée, le robot s'arrête.
        """
        if self.commands is None:
            # Plus de commandes : le robot reste arrêté
            self.robot.vitesse_gauche = 0
            self.robot.vitesse_droite = 0
            return

        cmd = self.commands[self.current_command_index]
        if cmd["type"] == "avancer":
            self.robot.vitesse_gauche = cmd["vitesse"]
            self.robot.vitesse_droite = cmd["vitesse"]
        elif cmd["type"] == "tourner":
            v = cmd["vitesse"]
            delta = cmd["delta"]
            self.robot.vitesse_gauche = v + delta
            self.robot.vitesse_droite = v - delta

        self.command_time_remaining -= delta_t
        if self.command_time_remaining <= 0:
            leftover = -self.command_time_remaining
            self.current_command_index += 1
            if self.current_command_index < len(self.commands):
                self.command_time_remaining = self.commands[self.current_command_index]["duration"]
                self.update_strategy(leftover)
            else:
                # Fin de la séquence : on arrête le robot
                self.commands = None
                self.robot.vitesse_gauche = 0
                self.robot.vitesse_droite = 0

    def afficher_console(self):
        """Affiche en continu la position, l'orientation et les vitesses du robot."""
        while True:
            print(f"Pos: ({self.robot.x:.1f}, {self.robot.y:.1f}) | Ori: {math.degrees(self.robot.orientation):.1f}° | V: G{self.robot.vitesse_gauche:.1f} D{self.robot.vitesse_droite:.1f}")
            time.sleep(0.1)

    def _update_frame(self):
        """Boucle d'actualisation (mode graphique) qui met à jour la physique et l'affichage."""
        if not self.use_graphics or not self.running:
            return
        current_time = time.time()
        delta_t = current_time - self.last_time
        self.last_time = current_time

        self.update_strategy(delta_t)
        # Mise à jour de la position et de l'orientation via la méthode mise_a_jour de arene.py
        self.arene.mise_a_jour(delta_t)
        # Ajoute le point actuel au trace
        self.trace_points.append((self.robot.x, self.robot.y))

        # Animation des roues (optionnel)
        left_dist = self.robot.vitesse_gauche * delta_t
        right_dist = self.robot.vitesse_droite * delta_t
        r = self.robot.diametre_roue / 2
        if r != 0:
            self.robot.angle_roue_gauche = (self.robot.angle_roue_gauche + left_dist / r) % (2 * math.pi)
            self.robot.angle_roue_droite = (self.robot.angle_roue_droite + right_dist / r) % (2 * math.pi)
        
        if self.view:
            self.view.update_affichage(self.robot, self.trace_points)
            self.view.after(10, self._update_frame)

    def run(self):
        """Lance la simulation en mode graphique ou console."""
        self.running = True
        if self.use_graphics and self.view:
            self.last_time = time.time()
            self.view.after(10, self._update_frame)
            self.view.mainloop()
            self.running = False
        else:
            # Mode console : lancer la séquence et l'exécuter en boucle
            self.demarrer_carre()
            print("Mode console. Séquence démarrée. Appuyez sur Ctrl+C pour arrêter.")
            last_time = time.time()
            try:
                while True:
                    current_time = time.time()
                    delta_t = current_time - last_time
                    last_time = current_time
                    self.update_strategy(delta_t)
                    self.arene.mise_a_jour(delta_t)
                    left_dist = self.robot.vitesse_gauche * delta_t
                    right_dist = self.robot.vitesse_droite * delta_t
                    r = self.robot.diametre_roue / 2
                    if r != 0:
                        self.robot.angle_roue_gauche = (self.robot.angle_roue_gauche + left_dist / r) % (2 * math.pi)
                        self.robot.angle_roue_droite = (self.robot.angle_roue_droite + right_dist / r) % (2 * math.pi)
                    time.sleep(0.01)
            except KeyboardInterrupt:
                self.running = False
                print("Simulation arrêtée.")

if __name__ == "__main__":
    choix = input("Voulez-vous activer l'affichage graphique ? (o/n) : ")
    use_graphics = choix.strip().lower() in ('o', 'oui', 'y', 'yes')
    sim = Simulation(use_graphics=use_graphics)
    # Pour lancer directement le dessin du carré, on peut appeler demarrer_carre()
    sim.demarrer_carre()
    sim.run()
