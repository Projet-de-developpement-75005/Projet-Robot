class Robot:
    def __init__(self, x=0, y=0, direction=0):
        """Initialise le robot à une position donnée avec une direction."""
        self.x = x
        self.y = y
        self.direction = direction  # En degrés : 0 = vers la droite

    def move(self, distance):
        """Fait avancer le robot dans la direction actuelle."""
        from math import cos, sin, radians
        self.x += distance * cos(radians(self.direction))
        self.y += distance * sin(radians(self.direction))

