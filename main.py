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
    def _init_(self, use_graphics=True):
        # Création de l'arène et du robot positionné au centre
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
        self.arene.ajouter_robot(self.robot)
        # Initialisation des angles pour l'animation des roues
        self.robot.angle_roue_gauche = 0.0
        self.robot.angle_roue_droite = 0.0

        self.use_graphics = use_graphics
        # Le robot est initialement à l'arrêt (mode "wait")
        self.mode = "wait"
        
        # Variables pour la séquence "square"
        self.commands = None
        self.current_command_index = 0
        self.command_time_remaining = 0
        
        # La trace sera enregistrée lors de l'exécution du carré
        self.trace_points = []

        self.running = False

        # Création de la vue graphique si nécessaire
        self.view = None
        if self.use_graphics:
            self.view = View(self.arene)
            # L'appui sur Entrée lance la séquence pour dessiner un carré
            self.view.bind("<Return>", self.lancer_square)
            # Démarrage d'un thread pour afficher les infos en console (optionnel)
            self.console_thread = Thread(target=self.afficher_console)
            self.console_thread.daemon = True
            self.console_thread.start()

    def lancer_square(self, event=None):
        """
        Passage en mode "square" :
          - Le robot démarre la séquence pour dessiner un carré.
        """
        self.mode = "square"
        self.demarrer_carre()

    def demarrer_carre(self, event=None):
        """
        Définit la séquence pour dessiner un carré :
          - Phase d'avance : 50 pixels à 20 px/s (2,5 s)
          - Phase de virage en arc : vitesse 20, décalage 10 
            (durée ≈ 1,57 s pour 90°)
        La trace est réinitialisée ici.
        """
        avancer_duration = 50 / 20.0  # 2,5 secondes
        delta = 10
        tourner_duration = (math.pi / 2) / ((2 * delta) / self.robot.distance_roues)
        
        # Construction de la séquence pour dessiner un carré (une seule fois)
        self.commands = []
        for _ in range(4):
            self.commands.append({"type": "avancer", "vitesse": 20, "duration": avancer_duration})
            self.commands.append({"type": "tourner", "vitesse": 20, "delta": delta, "duration": tourner_duration})
        self.current_command_index = 0
        self.command_time_remaining = self.commands[0]["duration"]
        # Réinitialiser la trace à partir du point de départ
        self.trace_points = [(self.robot.x, self.robot.y)]

    def update_strategy(self, delta_t):
        """
        Applique la commande active (mode "square") pendant sa durée.
        Une fois la séquence terminée, le robot s'arrête et la simulation se termine.
        """
        if self.commands is None or self.current_command_index >= len(self.commands):
            # Fin de la séquence : arrêt complet et fin de la simulation
            self.robot.vitesse_gauche = 0
            self.robot.vitesse_droite = 0
            self.running = False
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
                # Séquence terminée : arrêt complet
                self.robot.vitesse_gauche = 0
                self.robot.vitesse_droite = 0
                self.running = False

    def afficher_console(self):
        """Affiche en continu la position, l'orientation et les vitesses du robot."""
        while True:
            print(f"Pos: ({self.robot.x:.1f}, {self.robot.y:.1f}) | Ori: {math.degrees(self.robot.orientation):.1f}° | V: G{self.robot.vitesse_gauche:.1f} D{self.robot.vitesse_droite:.1f}")
            time.sleep(0.1)

    def _update_frame(self):
        """
        Boucle d'actualisation (mode graphique) :
         - En mode "wait", rien ne se passe (le robot reste à l'arrêt).
         - En mode "square", la séquence pour dessiner un carré est exécutée et
           la trajectoire est enregistrée et affichée.
        """
        if not self.use_graphics or not self.running:
            return
        current_time = time.time()
        delta_t = current_time - self.last_time
        self.last_time = current_time

        if self.mode == "square":
            if self.commands is not None:
                self.update_strategy(delta_t)
        
        # Mise à jour de la position et de l'orientation
        self.arene.mise_a_jour(delta_t)
        # En mode "square", on enregistre la trace
        if self.mode == "square":
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
            # Lancement de la boucle d'actualisation
            self.view.after(10, self._update_frame)
            self.view.mainloop()
        else:
            print("Mode console: appuyez sur Ctrl+C pour arrêter.")
            self.running = True
            last_time = time.time()
            try:
                while True:
                    current_time = time.time()
                    delta_t = current_time - last_time
                    last_time = current_time
                    if self.mode == "square" and self.commands is not None:
                        self.update_strategy(delta_t)
                    self.arene.mise_a_jour(delta_t)
                    time.sleep(0.01)
                    if not self.running and self.mode == "square":
                        break
            except KeyboardInterrupt:
                self.running = False
                print("Simulation arrêtée.")

if _name_ == "_main_":
    choix = input("Voulez-vous activer l'affichage graphique ? (o/n) : ")
    use_graphics = choix.strip().lower() in ('o', 'oui', 'y', 'yes')
    
    def mise_a_jour_arene(self, delta_t):
        if self.robot:
            self.robot.mettre_a_jour_position(delta_t)
            for obs in self.obstacles:
                if obs.est_en_collision(self.robot.x, self.robot.y):
                    print("Collision détectée ! Le robot doit s'arrêter.")
                    self.robot.vitesse_gauche = 0
                    self.robot.vitesse_droite = 0
    Arene.mise_a_jour = mise_a_jour_arene

    sim = Simulation(use_graphics=use_graphics)
    sim.run()