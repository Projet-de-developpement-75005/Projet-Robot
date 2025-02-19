import time
from Interface import Interface
from Robot import Robot
from Controller import Controller

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
            self.controleur.boucle_simulation(self.interface)  # Passer l'interface à la boucle
        else:
            self.controleur.demander_controle_utilisateur()  # Demander à l'utilisateur s'il veut entrer les vitesses
            self.boucle_simulation()

    def boucle_simulation(self):
        """Gère la simulation dans le mode classique."""
        while True:
            self.controleur.deplacer(self.obstacles)  # Déplacer le robot avec les obstacles
            self.interface.rafraichir_ecran(self.robot, self.obstacles, time.time() - self.temps_depart)
            time.sleep(0.03)

    