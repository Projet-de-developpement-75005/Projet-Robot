class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = 0  # Orientation en degrés (0 = droite, 90 = haut, 180 = gauche, 270 = bas)


    def afficher_position(self):
        print(f"Position actuelle : ({self.x}, {self.y}), Orientation : {self.orientation}°")

   
    def tourner(self, angle):
        """Tourne le robot d'un certain angle (en degrés)"""
        self.orientation = (self.orientation + angle) % 360
        print(f"Orientation actuelle : {self.orientation}°")