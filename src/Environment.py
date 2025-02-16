class Environment:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.obstacles = [
            (200, 300, 50, 50),  # Obstacle 1: (x, y, largeur, hauteur)
            (500, 400, 60, 60),  # Obstacle 2
            (700, 200, 40, 40)   # Obstacle 3
        ]
