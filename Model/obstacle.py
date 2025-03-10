class Obstacle:
    def __init__(self, x, y, radius=1):
        """Initialise un obstacle avec une position et un rayon."""
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return f"Obstacle(pos=({self.x}, {self.y}), radius={self.radius})"