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
        self.rayon = distance_roues / 2  # Rayon du robot pour la détection de collision
        
        # Attribut pour suivre la distance totale parcourue
        self.distance_parcourue = 0.0

    def mettre_a_jour_position(self, delta_t):
        # Calcul de la vitesse moyenne
        vitesse_moyenne = (self.vitesse_gauche + self.vitesse_droite) / 2.0
        
        # Calcul du changement d'orientation
        delta_orientation = (self.vitesse_droite - self.vitesse_gauche) / self.distance_roues
        self.orientation += delta_orientation * delta_t
        
        # Mise à jour de la position selon l'orientation mise à jour
        self.x += vitesse_moyenne * delta_t * math.cos(self.orientation)
        self.y += vitesse_moyenne * delta_t * math.sin(self.orientation)
        
        # Mise à jour de la distance parcourue
        # On applique la règle : distance = vitesse * temps.
        # On prend la valeur absolue pour toujours accumuler la distance positive parcourue.
        self.distance_parcourue += abs(vitesse_moyenne * delta_t)

    def set_vitesses(self, vitesse_gauche, vitesse_droite):
        print("Mise à jour des vitesses: Gauche =", vitesse_gauche, "| Droite =", vitesse_droite)
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite

    def get_distance(self):
        """
        Retourne la distance totale parcourue par le robot.
        """
        return self.distance_parcourue
