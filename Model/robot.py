class Robot:
    def __init__(self, x=0, y=0, direction=0):
        """Initialise le robot à une position donnée avec une direction."""
        self.x = x
        self.y = y
        self.direction = direction  # En degrés : 0 = vers la droite

    def __str__(self):
        return f"Robot(pos=({self.x:.2f}, {self.y:.2f}), dir={self.direction}°)"