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
    
    def mettre_a_jour_position(self, delta_t):
        """
        Met à jour la position et l'orientation du robot en fonction des vitesses linéaires.
        delta_t : intervalle de temps pendant lequel les vitesses sont appliquées (en secondes)
        """
        # Sauvegarde de la position avant déplacement
        old_x, old_y = self.x, self.y

        # Calcul de la vitesse linéaire moyenne
        vitesse_moyenne = (self.vitesse_gauche + self.vitesse_droite) / 2
        
        # La vitesse angulaire (rad/s) est calculée à partir de la différence des vitesses linéaires
        delta_orientation = (self.vitesse_droite - self.vitesse_gauche) / self.distance_roues

        # Mise à jour de l'orientation et de la position
        self.orientation += delta_orientation * delta_t
        self.x += vitesse_moyenne * delta_t * math.cos(self.orientation)
        self.y += vitesse_moyenne * delta_t * math.sin(self.orientation)
        
        # Mise à jour de la distance parcourue
        dx = self.x - old_x
        dy = self.y - old_y
        self.distance_parcourue += math.sqrt(dx**2 + dy**2)
    
    def set_vitesses(self, vitesse_gauche, vitesse_droite):
        """
        Met à jour les vitesses linéaires des roues.
        """
        print("Mise à jour des vitesses: Gauche =", vitesse_gauche, "| Droite =", vitesse_droite)
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        
    def capteur_distance(self, obstacles, max_range=100, step=1):
        """
        Simule un capteur de distance qui détecte un obstacle dans la direction du robot.
        Pour chaque distance d'incrément 'step' allant de 0 à max_range, on calcule le point
        potentiel et on vérifie s'il est à l'intérieur d'un obstacle.
        
        Args:
            obstacles (list): Liste d'obstacles, chaque obstacle doit avoir des attributs x, y et radius.
            max_range (float): Distance maximale à détecter (par défaut 100).
            step (float): Incrément de distance pour la détection (par défaut 1).

        Returns:
            float: La distance parcourue jusqu'au premier obstacle détecté, ou max_range si aucun obstacle n'est rencontré.
        """
        for d in range(0, int(max_range), int(step)):
            test_x = self.x + d * math.cos(self.orientation)
            test_y = self.y + d * math.sin(self.orientation)
            for obs in obstacles:
                # Calcul de la distance entre le point de test et le centre de l'obstacle
                dist = math.sqrt((test_x - obs.x) ** 2 + (test_y - obs.y) ** 2)
                if dist <= obs.radius:
                    return d  # Obstacle détecté à la distance d
        return max_range
    
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
    
    def get_vitesses_angulaires(self):
        """
        Retourne les vitesses angulaires des roues en rad/s, calculées à partir des vitesses linéaires.
        """
        rayon_roue = self.diametre_roue / 2
        vitesse_angulaire_gauche = self.vitesse_gauche / rayon_roue
        vitesse_angulaire_droite = self.vitesse_droite / rayon_roue
        return (vitesse_angulaire_gauche, vitesse_angulaire_droite)
    
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
    
    def get_x_step(self):
        return self.x

    def get_y_step(self):
        return self.y
    
    def get_distance(self):
        """
        Retourne la distance totale parcourue par le robot depuis son initialisation.
        """
        return self.distance_parcourue
