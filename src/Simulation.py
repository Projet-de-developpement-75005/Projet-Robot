import time
from Interface import Interface
from Robot import Robot
from Controller import Controleur

class EnvRobot:
    def __init__(self, canvas, largeur=900, hauteur=800, mode=2):
        self.largeur = largeur
        self.hauteur = hauteur      
        self.robot = Robot(self.largeur // 2, self.hauteur // 2)
        self.controleur = Controleur(self.robot, self)  # Passer self (envi
        self.interface = Interface(canvas, self.largeur, self.hauteur)

        self.mode = mode
        if self.mode == 1:
            self.cote_parcouru = 0
            self.cote_carre = 100
            self.cote_courant = 1
        elif self.mode == 2:
            self.controleur.activer_controle_clavier(canvas)
        # Ajout des obstacles
        self.obstacles = [
            (200, 300, 50, 50),  # Obstacle 1: (x, y, largeur, hauteur)
            (500, 400, 60, 60),  # Obstacle 2
            (700, 200, 40, 40)   # Obstacle 3
        ]


    def demarrer_simulation(self):
        """Démarre la simulation en fonction du mode choisi."""
        self.temps_depart = time.time()

        if self.mode == 1:
            self.deplacement_carre()
        else:
            self.boucle_simulation()

    def boucle_simulation(self):
        while True:
            self.robot.deplacer(self.environnement.obstacles)
            self.robot.limiter_position(self.largeur, self.hauteur)
            temps_ecoule = time.time() - self.temps_depart
            self.interface.rafraichir_ecran(self.robot, self.environnement.obstacles, temps_ecoule)
            time.sleep(0.03)
    def demander_controle_utilisateur(self):
        print("Voulez-vous entrer manuellement les vitesses des roues ? (o/n)")
        choix = input().lower()
        if choix == "o":
            self.robot.vitesse_roue_gauche = float(input("Entrez la vitesse de la roue gauche (-8 à 8) : "))
            self.robot.vitesse_roue_droite = float(input("Entrez la vitesse de la roue droite (-8 à 8) : "))
        else:
            print("Utilisez les touches du clavier pour contrôler la voiture.")
            self.activer_controle_clavier()
                

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

    def activer_controle_clavier(self):
        """Ajoute des touches pour contrôler le robot avec ZQSD (ou flèches)."""
        self.interface.canvas.bind_all("<Up>", lambda e: self.set_vitesse(3, 3))
        self.interface.canvas.bind_all("<Down>", lambda e: self.set_vitesse(-3, -3))
        self.interface.canvas.bind_all("<Left>", lambda e: self.set_vitesse(-2, 2))
        self.interface.canvas.bind_all("<Right>", lambda e: self.set_vitesse(2, -2))
        self.interface.canvas.bind_all("<space>", lambda e: self.set_vitesse(0, 0))
        
    def set_vitesse(self, gauche, droite):
        self.robot.vitesse_roue_gauche = gauche
        self.robot.vitesse_roue_droite = droite