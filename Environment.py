class Environment:
    def __init__(self, largeur, longueur, obstacles):
        self.largeur = largeur
        self.longueur = longueur
        self.obstacles = obstacles

    def est_valide_position(self, x, y):
        """Vérifie si une position est valide (pas d'obstacle, pas hors des limites)"""
        if x < 0 or x >= self.largeur or y < 0 or y >= self.longueur:
            return False
        if (x, y) in self.obstacles:
            return False
        return True