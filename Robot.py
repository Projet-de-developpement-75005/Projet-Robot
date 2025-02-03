class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0  # Orientation de la voiture
        self.vitesse_roue_gauche = 0  # Vitesse de la roue gauche
        self.vitesse_roue_droite = 0  # Vitesse de la roue droite


    def afficher_position(self):
        print(f"Position actuelle : ({self.x}, {self.y}), Orientation : {self.orientation}°")

   
    def tourner(self, angle):
        """Tourne le robot d'un certain angle (en degrés)"""
        self.orientation = (self.orientation + angle) % 360
        print(f"Orientation actuelle : {self.orientation}°")