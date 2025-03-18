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
        obstacle1 = Obstacle(100, 100, 50, 50)
        obstacle2 = Obstacle(300, 200, 30, 60)
        self.arene.ajouter_obstacle(obstacle1)
        self.arene.ajouter_obstacle(obstacle2)
        self.arene.ajouter_robot(self.robot)
        # Initialisation des angles des roues pour l'animation (optionnel)
        self.robot.angle_roue_gauche = 0.0
        self.robot.angle_roue_droite = 0.0

        self.use_graphics = use_graphics
        # Liste des commandes pour dessiner le carré
        self.commands = None
        self.current_command_index = 0
        self.command_time_remaining = 0
        self.running = False
        # Liste des points de la trajectoire (pour tracer le trait vert)
        self.trace_points = []

        # Création de la vue si nécessaire
        self.view = None
        if self.use_graphics:
            self.view = View(self.arene)
            # Appuyer sur Entrée dans la fenêtre lancera la séquence
            self.view.bind("<Return>", self.demarrer_carre)
            # Démarrer le thread d'affichage console
            self.console_thread = Thread(target=self.afficher_console)
            self.console_thread.daemon = True
            self.console_thread.start()

    def demarrer_carre(self, event=None):
        """
        Définit une séquence de commandes pour que le robot "dessine" un carré.
        Chaque cycle comporte :
         - Une phase d'avance (50 pixels à 10 px/s)
         - Une phase de virage en arc (vitesse de base 10 et décalage delta = 5)
        """
        avancer_duration = 50 / 10.0  # 5 secondes
        delta = 5
        # Calcul de la durée pour tourner 90° :
        tourner_duration = (math.pi / 2) / ((2 * delta) / self.robot.distance_roues)
        
        # Construction de la séquence pour dessiner un carré (une fois)
        self.commands = []
        for _ in range(4):
            self.commands.append({"type": "avancer", "vitesse": 10, "duration": avancer_duration})
            self.commands.append({"type": "tourner", "vitesse": 10, "delta": delta, "duration": tourner_duration})
        self.current_command_index = 0
        self.command_time_remaining = self.commands[0]["duration"]
        # Réinitialiser le trace (on garde le premier point)
        self.trace_points = [(self.robot.x, self.robot.y)]

    def update_strategy(self, delta_t):
        """
        Applique la commande active pendant sa durée.
        Pour "avancer", les deux roues tournent à la même vitesse.
        Pour "tourner", on fixe : vitesse gauche = vitesse + delta, vitesse droite = vitesse - delta.
        Lorsque le temps est écoulé, on passe à la commande suivante.
        """
        if self.commands is None or self.current_command_index >= len(self.commands):
            self.demarrer_carre()  # redémarre la séquence
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
                self.demarrer_carre()

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

        if self.commands is not None:
            self.update_strategy(delta_t)
        
        # Mise à jour de la position et de l'orientation du robot
        self.arene.mise_a_jour(delta_t)
        # Ajoute la position actuelle au trace
        self.trace_points.append((self.robot.x, self.robot.y))

        # Mise à jour de l'animation des roues (optionnel)
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
            # Mode console : la séquence démarre immédiatement
            self.demarrer_carre()
            print("Mode console. Séquence démarrée. Appuyez sur Ctrl+C pour arrêter.")
            last_time = time.time()
            try:
                while True:
                    current_time = time.time()
                    delta_t = current_time - last_time
                    last_time = current_time
                    if self.commands is not None:
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
    
    # Redéfinition de la méthode de mise à jour de l'arène
    def mise_a_jour_arene(self, delta_t):
        if self.robot:
            # Calculer la nouvelle position du robot
            nouvelle_x = self.robot.x + self.robot.vitesse_gauche * delta_t * math.cos(self.robot.orientation)
            nouvelle_y = self.robot.y + self.robot.vitesse_gauche * delta_t * math.sin(self.robot.orientation)

            # Vérifier les collisions avec les obstacles
            collision = False
            for obstacle in self.obstacles:
                if obstacle.est_en_collision(nouvelle_x, nouvelle_y, self.robot.rayon):
                    print("Collision détectée ! Le robot doit s'arrêter.")
                    collision = True
                    break

            # Si aucune collision n'est détectée, mettre à jour la position
            if not collision:
                self.robot.x = nouvelle_x
                self.robot.y = nouvelle_y
            else:
                # Arrêter le robot en cas de collision
                self.robot.vitesse_gauche = 0
                self.robot.vitesse_droite = 0
    Arene.mise_a_jour = mise_a_jour_arene
    
    sim = Simulation(use_graphics=use_graphics)
    sim.run()