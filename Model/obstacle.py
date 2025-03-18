class Obstacle:
    def __init__(self, x, y, largeur, hauteur):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

    def est_en_collision(self, robot_x, robot_y):
        return self.x <= robot_x <= self.x + self.largeur and self.y <= robot_y <= self.y + self.hauteur