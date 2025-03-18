from math import radians, cos, sin

class Robot:
    def __init__(self, x=0, y=0, direction=0):
        """
        Initialise le robot à une position donnée et avec une direction (en degrés).
        Un attribut 'trace' mémorise l'historique des positions pour dessiner le parcours.
        """
        self.x = x
        self.y = y
        self.direction = direction  # En degrés : 0 = vers la droite
        self.trace = [(x, y)]
        self.rayon = 5  # Rayon pour le dessin du robot
        self.step_size = 5  # Taille d'un pas (pour avancer)

    def move_forward(self, distance):
        """
        Fait avancer le robot d'une distance donnée.
        Le robot avance en fonction de sa direction actuelle.
        """
        dx = distance * cos(radians(self.direction))
        dy = distance * sin(radians(self.direction))
        self.x += dx
        self.y += dy
        self.trace.append((self.x, self.y))

    def rotate(self, angle):
        """
        Fait tourner le robot d'un angle donné (en degrés).
        """
        self.direction = (self.direction + angle) % 360

    def __str__(self):
        return f"Robot(x={self.x:.2f}, y={self.y:.2f}, dir={self.direction}°)"
