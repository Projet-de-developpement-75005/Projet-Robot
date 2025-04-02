import math

class Robot:
    def __init__(self, x, y, orientation, vitesse_gauche, vitesse_droite, diametre_roue, distance_roues):
        self.x = x  # Position en X
        self.y = y  # Position en Y
        self.orientation = orientation  # Angle en radians
        self.vitesse_gauche = vitesse_gauche  # Vitesse linéaire de la roue gauche (m/s)
        self.vitesse_droite = vitesse_droite  # Vitesse linéaire de la roue droite (m/s)
        self.diametre_roue = diametre_roue  # Diamètre de la roue (m)
        self.distance_roues = distance_roues  # Distance entre les roues (m)
        self.rayon = distance_roues / 2  # Rayon du robot pour la détection de collision (m)
        self.distance_parcourue = 0.0  # Distance totale parcourue (m)
    

    
    def set_vitesses(self, vitesse_gauche, vitesse_droite):
        """
        Met à jour les vitesses linéaires des roues.
        """
        print("Mise à jour des vitesses: Gauche =", vitesse_gauche, "| Droite =", vitesse_droite)
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        
    
    def tourner(self, dt):
        """
        Fait tourner le robot sur l'intervalle de temps dt en utilisant ses vitesses linéaires.
        On suppose que pour tourner sur place, les vitesses sont réglées de manière opposée.
        
        dt : intervalle de temps pendant lequel les vitesses sont appliquées (en secondes)
        """
        # Calcul de la vitesse angulaire à partir des vitesses linéaires
        delta_orientation = (self.vitesse_droite - self.vitesse_gauche) / self.distance_roues
        self.orientation += delta_orientation * dt
        print(f"Tourner => Orientation: {math.degrees(self.orientation):.2f}°")
    
    def avancer(self, dt):
        """
        Déplace le robot en appliquant ses vitesses linéaires sur un intervalle dt (en secondes).
        """
        old_x, old_y = self.x, self.y

        # Calcul de la vitesse linéaire moyenne
        vitesse_moyenne = (self.vitesse_gauche + self.vitesse_droite) / 2
        # Calcul de la vitesse angulaire (rad/s) pour mettre à jour l'orientation
        delta_orientation = (self.vitesse_droite - self.vitesse_gauche) / self.distance_roues

        # Mise à jour de l'orientation et de la position
        self.orientation += delta_orientation * dt
        self.x += vitesse_moyenne * dt * math.cos(self.orientation)
        self.y += vitesse_moyenne * dt * math.sin(self.orientation)

        # Mise à jour de la distance parcourue
        dx = self.x - old_x
        dy = self.y - old_y
        self.distance_parcourue += math.sqrt(dx**2 + dy**2)
        
        print(f"Avancer => Position: ({self.x:.2f}, {self.y:.2f}), Orientation: {math.degrees(self.orientation):.2f}°")
    
    
    def get_distance(self):
        """
        Retourne la distance totale parcourue par le robot depuis son initialisation.
        """
        return self.distance_parcourue
