class Obstacle:
    def __init__(self, x, y, largeur, hauteur):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

    def est_en_collision(self, robot_x, robot_y, robot_rayon):
        """
        Vérifie si le robot entre en collision avec l'obstacle.
        :param robot_x: Position x du robot
        :param robot_y: Position y du robot
        :param robot_rayon: Rayon du robot (pour une détection circulaire)
        :return: True si collision, False sinon
        """
        # Trouver le point le plus proche de l'obstacle par rapport au robot
        closest_x = max(self.x, min(robot_x, self.x + self.largeur))
        closest_y = max(self.y, min(robot_y, self.y + self.hauteur))

        # Calculer la distance entre le robot et ce point
        distance_x = robot_x - closest_x
        distance_y = robot_y - closest_y

        # Vérifier si la distance est inférieure au rayon du robot
        return (distance_x ** 2 + distance_y ** 2) <= (robot_rayon ** 2)