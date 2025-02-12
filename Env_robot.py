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

        # Suivi du temps et des touches pressées
        self.temps_depart = time.time()
        self.touches_pressees = set()  # Initialisation des touches pressées
        # Choix du mode de déplacement
        self.mode_deplacement = input("Choisissez le mode de déplacement : \n1 - Carré \n2 - Mode classique \nEntrez votre choix (1 ou 2): ")
        if self.mode_deplacement == "1":
            self.cote_carre = 100  # Longueur d'un côté du carré
            self.cote_parcouru = 0
            self.cote_courant = 1
        else:
            self.cote_carre = None  # Mode classique, pas de carré
            self.choix_controle = input("Voulez-vous entrer manuellement les vitesses et la direction ? (o/n) : ").lower()
            
            if self.choix_controle == "o":
                self._initialiser_vitesses_manuellement()
                self.controle_clavier = False
            else:
                self.controle_clavier = True


            # Événements clavier
            self.root.bind_all("<KeyPress>", self._on_key_press)
            self.root.bind_all("<KeyRelease>", self._on_key_release)
        def _on_key_press(self, event):
            """Ajoute la touche pressée à touches_pressees"""
            self.touches_pressees.add(event.keysym)

       
        def _on_key_release(self, event):
            """Retire la touche relâchée de touches_pressees"""
            self.touches_pressees.discard(event.keysym)
        
        def _initialiser_vitesses_manuellement(self):
            """Initialise les vitesses et la direction du robot en mode classique (manuel)."""
            self.robot.vitesse_roue_gauche = int(input("Entrez la vitesse de la roue gauche (-8 à 8) : "))
            self.robot.vitesse_roue_droite = int(input("Entrez la vitesse de la roue droite (-8 à 8) : "))
            
            direction = input("Entrez la direction (haut, bas, gauche, droite) : ").lower()
            self.robot.angle = {"haut": 90, "bas": 270, "gauche": 180, "droite": 0}.get(direction, 90)

        def demarrer_simulation(self):
            """Démarre la simulation, selon le mode de déplacement choisi."""
            while True:
                if self.mode_deplacement == "1":
                    # Déplacer le robot sur la trajectoire carrée en respectant les limites
                    self._deplacer_trajectoire_carre()
                else:
                    if self.controle_clavier:
                        self._gerer_deplacement_clavier()

            # Effectuer le déplacement et limiter la position du robot
            self.robot.deplacer(self.environnement.obstacles)
            self.robot.limiter_position(self.largeur, self.hauteur)  # Limiter la position

            # Rafraîchir l'écran de la simulation
            temps_ecoule = time.time() - self.temps_depart
            self.interface.rafraichir_ecran(self.robot, self.environnement.obstacles, temps_ecoule)

            # Mettre à jour l'interface graphique
            self.root.update_idletasks()
            self.root.update()
            time.sleep(0.02)

        def _deplacer_trajectoire_carre(self):
            """Déplace le robot sur une trajectoire en carré tout en vérifiant les limites."""
            if self.cote_parcouru < self.cote_carre:
                # Avancer dans la direction actuelle
                self.robot.vitesse_roue_gauche = self.robot.vitesse_roue_droite = 5  # Vitesse de déplacement
                self.cote_parcouru += 1
            else:
              # Après avoir parcouru un côté, tourner de 90°
              self.robot.angle += 90
              self.cote_courant = (self.cote_courant % 4) + 1
              self.cote_parcouru = 0

        def _gerer_deplacement_clavier(self):
            """Gère les déplacements du robot via le clavier en mode classique."""
            if "Up" in self.touches_pressees:
                self.robot.vitesse_roue_gauche = self.robot.vitesse_roue_droite = 5
            elif "Down" in self.touches_pressees:
                self.robot.vitesse_roue_gauche = self.robot.vitesse_roue_droite = -5
            elif "Left" in self.touches_pressees:
                self.robot.vitesse_roue_gauche = -3
                self.robot.vitesse_roue_droite = 3
            elif "Right" in self.touches_pressees:
                self.robot.vitesse_roue_gauche = 3
                self.robot.vitesse_roue_droite = -3
            else:
                self.robot.vitesse_roue_gauche = 0
                self.robot.vitesse_roue_droite = 0
            # Calculer le temps écoulé
            temps_ecoule = time.time() - self.temps_depart

            # Rafraîchir l'interface avec le temps écoulé
            self.interface.rafraichir_ecran(self.robot, self.environnement.obstacles, temps_ecoule)
            self.clock.tick(30)

    pygame.quit()
