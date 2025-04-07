import math

class Robot:
    def __init__(self, x, y, orientation, vitesse_gauche, vitesse_droite, diametre_roue, distance_roues):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.diametre_roue = diametre_roue
        self.distance_roues = distance_roues
        self.rayon = distance_roues / 2
        self.distance_parcourue = 0.0
        #pour la q1.3
        self.crayon_baisse = False
        self.trace = [] #la liste pour la trace
        self.crayon_baisse = False
        #pour la q1.4
        self.couleur_trace = "blue"  #couleur bleue active
        self.couleurs_trace = []  #liste traces pour les couleurs


    #ajout pour la q1.3
    def dessine(self, b: bool):
        self.crayon_baisse = b

    def rouge(self):
        self.couleur_trace = "red"

    def bleu(self):
        self.couleur_trace = "blue"


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
