import math

# Define constants for the robot size
ROBOT_LONGUEUR = 50  # Robot length (in pixels)
ROBOT_LARGEUR = 30   # Robot width (in pixels)

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # Orientation du robot
        self.vitesse_roue_gauche = 0
        self.vitesse_roue_droite = 0

    def verifier_collision(self, obstacles):
        """Vérifie si le robot entre en collision avec un obstacle."""
        robot_rect = self.obtenir_rect()
        for obstacle in obstacles:
            if (robot_rect[0] < obstacle[0] + obstacle[2] and
                robot_rect[0] + robot_rect[2] > obstacle[0] and
                robot_rect[1] < obstacle[1] + obstacle[3] and
                robot_rect[1] + robot_rect[3] > obstacle[1]):
                return True
        return False

    def deplacer(self, obstacles):
        """Déplace le robot en fonction des vitesses des roues."""
        ancien_x, ancien_y = self.x, self.y
        vitesse_moyenne = (self.vitesse_roue_gauche + self.vitesse_roue_droite) / 2
        difference_vitesse = self.vitesse_roue_droite - self.vitesse_roue_gauche

        self.angle += difference_vitesse * 0.5  # Rotation
        self.x += math.cos(math.radians(self.angle)) * vitesse_moyenne
        self.y += math.sin(math.radians(self.angle)) * vitesse_moyenne

        if self.verifier_collision(obstacles):
            self.x, self.y = ancien_x, ancien_y

    def obtenir_rect(self):
        """Retourne le rectangle de collision du robot."""
        return (
            self.x - ROBOT_LONGUEUR // 2,
            self.y - ROBOT_LARGEUR // 2,
            ROBOT_LONGUEUR,
            ROBOT_LARGEUR
        )

    def limiter_position(self, largeur_fenetre, hauteur_fenetre):
        """Empêche le robot de sortir des limites de la fenêtre."""
        self.x = max(ROBOT_LONGUEUR // 2, min(self.x, largeur_fenetre - ROBOT_LONGUEUR // 2))
        self.y = max(ROBOT_LARGEUR // 2, min(self.y, hauteur_fenetre - ROBOT_LARGEUR // 2))

    def calculer_distance_restante(self, largeur_fenetre, hauteur_fenetre, obstacles):
        """Calculer la distance restante jusqu'aux limites de la fenêtre ou aux obstacles."""
        # Distance jusqu'aux bords de la fenêtre
        distance_bord = min(self.x, largeur_fenetre - self.x, self.y, hauteur_fenetre - self.y)

        # Vérification de la distance aux obstacles
        for obstacle in obstacles:
            obstacle_x, obstacle_y, obstacle_largeur, obstacle_hauteur = obstacle
            distance_obstacle = math.sqrt((self.x - obstacle_x) ** 2 + (self.y - obstacle_y) ** 2)
            distance_bord = min(distance_bord, distance_obstacle)

        return distance_bord
import math

ROBOT_LONGUEUR = 60
ROBOT_LARGEUR = 30

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # Orientation du robot
        self.vitesse_roue_gauche = 0
        self.vitesse_roue_droite = 0

    def verifier_collision(self, obstacles):
        """Vérifie si le robot entre en collision avec un obstacle."""
        robot_rect = self.obtenir_rect()
        for obstacle in obstacles:
            if (robot_rect[0] < obstacle[0] + obstacle[2] and
                robot_rect[0] + robot_rect[2] > obstacle[0] and
                robot_rect[1] < obstacle[1] + obstacle[3] and
                robot_rect[1] + robot_rect[3] > obstacle[1]):
                return True
        return False

    def deplacer(self, obstacles):
        """Déplace le robot en fonction des vitesses des roues."""
        ancien_x, ancien_y = self.x, self.y
        vitesse_moyenne = (self.vitesse_roue_gauche + self.vitesse_roue_droite) / 2
        difference_vitesse = self.vitesse_roue_droite - self.vitesse_roue_gauche

        self.angle += difference_vitesse * 0.5  # Rotation
        self.x += math.cos(math.radians(self.angle)) * vitesse_moyenne
        self.y += math.sin(math.radians(self.angle)) * vitesse_moyenne

        if self.verifier_collision(obstacles):
            self.x, self.y = ancien_x, ancien_y

    def obtenir_rect(self):
        """Retourne le rectangle de collision du robot."""
        return (
            self.x - ROBOT_LONGUEUR // 2,
            self.y - ROBOT_LARGEUR // 2,
            ROBOT_LONGUEUR,
            ROBOT_LARGEUR
        )

    def limiter_position(self, largeur_fenetre, hauteur_fenetre):
        """Empêche le robot de sortir des limites de la fenêtre."""
        self.x = max(ROBOT_LONGUEUR // 2, min(self.x, largeur_fenetre - ROBOT_LONGUEUR // 2))
        self.y = max(ROBOT_LARGEUR // 2, min(self.y, hauteur_fenetre - ROBOT_LARGEUR // 2))
