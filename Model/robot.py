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
    def mettre_a_jour_position(self, delta_t):
        # Mise à jour de la position et de l'orientation du robot en fonction des vitesses des roues
        vitesse_moyenne = (self.vitesse_gauche + self.vitesse_droite) / 2
        delta_orientation = (self.vitesse_droite - self.vitesse_gauche) / self.distance_roues

        self.orientation += delta_orientation * delta_t
        self.x += vitesse_moyenne * delta_t * math.cos(self.orientation)
        self.y += vitesse_moyenne * delta_t * math.sin(self.orientation)
        
    def set_vitesses(self, vitesse_gauche, vitesse_droite):
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
    
    def tourner(self, angle):
        """
        Tourne le robot de l'angle spécifié (en degrés).
        Un angle positif effectue une rotation anti-horaire.
        Cette méthode met à jour instantanément l'orientation du robot.
        """
        # Conversion de l'angle en radians
        angle_rad = math.radians(angle)
        self.orientation += angle_rad

    def avancer(self, dt):
        """
        Déplace le robot en utilisant ses vitesses angulaires stockées.

        dt : intervalle de temps pendant lequel les roues tournent (en secondes)
        
        La méthode convertit les vitesses angulaires en vitesses linéaires grâce au diamètre de la roue.
        """
        # Calcul du rayon de la roue à partir du diamètre
        rayon_roue = self.diametre_roue / 2
        
        # Conversion des vitesses angulaires (stockées dans self) en vitesses linéaires
        vitesse_lineaire_gauche = rayon_roue * self.vitesse_gauche
        vitesse_lineaire_droite = rayon_roue * self.vitesse_droite
        
        # Calcul de la vitesse linéaire moyenne et du changement d'orientation
        vitesse_moyenne = (vitesse_lineaire_gauche + vitesse_lineaire_droite) / 2
        delta_orientation = (vitesse_lineaire_droite - vitesse_lineaire_gauche) / self.distance_roues
        
        # Mise à jour de l'orientation et de la position
        self.orientation += delta_orientation * dt
        self.x += vitesse_moyenne * dt * math.cos(self.orientation)
        self.y += vitesse_moyenne * dt * math.sin(self.orientation)
        
        print(f"Avancer => Position: ({self.x:.2f}, {self.y:.2f}), Orientation: {math.degrees(self.orientation):.2f}°")