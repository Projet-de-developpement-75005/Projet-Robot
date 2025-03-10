
class Arena:
    def __init__(self, width=100, height=100):
        """Initialise l'arène avec des dimensions et une liste d'obstacles."""
        self.width = width
        self.height = height
        self.obstacles = []

    def add_obstacle(self, obstacle):
        """Ajoute un obstacle à l'arène."""
        self.obstacles.append(obstacle)

    def __str__(self):
        return f"Arena({self.width}x{self.height}, {len(self.obstacles)} obstacles)"