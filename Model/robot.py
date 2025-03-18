import math
class Robot:
    def __init__(self, x, y, orientation, vitesse_gauche, vitesse_droite, diametre_roue, distance_roues):
        self.x = x  # Position en X
        self.y = y  # Position en Y
        self.orientation = orientation  # Angle en radians
        self.vitesse_gauche = vitesse_gauche  # Vitesse de la roue gauche
        self.vitesse_droite = vitesse_droite  # Vitesse de la roue droite
        self.diametre_roue = diametre_roue
        self.distance_roues = distance_roues

    