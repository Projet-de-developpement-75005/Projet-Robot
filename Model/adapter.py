from .robot import Robot

class Proxy_Virtuel:
    def __init__(self, robot, obstacles=None):
        self.robot = robot
        self.obstacles = obstacles if obstacles is not None else []
        self._distance = 0
        self._angle = 0

    def set_vitesse(self, vitesse_gauche, vitesse_droite):
        self.robot.set_vitesses(vitesse_gauche, vitesse_droite)
    
    def update_distance(self):
        # On utilise le déplacement linéaire moyen pour simuler la distance parcourue
        rayon_roue = self.robot.diametre_roue / 2
        vitesse_gauche_lin = self.robot.vitesse_gauche * rayon_roue
        vitesse_droite_lin = self.robot.vitesse_droite * rayon_roue
        vitesse_moyenne = (vitesse_gauche_lin + vitesse_droite_lin) / 2
        self._distance += abs(vitesse_moyenne)


