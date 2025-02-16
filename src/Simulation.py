import time
from Environment import Environment
from Robot import Robot
from Interface import Interface

class EnvRobot:
    def __init__(self, canvas, largeur=900, hauteur=800, mode=2):
        self.largeur = largeur
        self.hauteur = hauteur
        self.environnement = Environment(self.largeur, self.hauteur)
        self.robot = Robot(self.largeur // 2, self.hauteur // 2)
        self.interface = Interface(canvas, self.largeur, self.hauteur)

        self.mode = mode
        if self.mode == 2:
            self.demander_controle_utilisateur()


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