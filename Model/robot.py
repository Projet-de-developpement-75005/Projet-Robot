from math import radians, cos, sin

class Robot:
    def __init__(self, x=0, y=0, direction=0):
        """
        Initialise le robot à une position (x, y) avec une direction (en degrés).
        La trace garde en mémoire les positions du robot uniquement si trace_active est True.
        """
        self.x = x
        self.y = y
        self.direction = direction  # 0° vers la droite
        self.trace = []             # Historique des positions (pour le dessin du carré)
        self.trace_active = False   # Active l'enregistrement de la trace uniquement en dessinant le carré
        self.rayon = 5              # Rayon du robot pour l'affichage
        self.step_size = 5          # Taille du pas pour le déplacement

    def move_forward(self, distance):
        """
        Fait avancer le robot d'une distance donnée selon sa direction actuelle.
        Ajoute la nouvelle position à la trace uniquement si trace_active est True.
        """
        dx = distance * cos(radians(self.direction))
        dy = distance * sin(radians(self.direction))
        self.x += dx
        self.y += dy
        if self.trace_active:
            self.trace.append((self.x, self.y))

    def rotate(self, angle):
        """Fait tourner le robot d'un angle donné (en degrés)."""
        self.direction = (self.direction + angle) % 360

    def __str__(self):
        return f"Robot(x={self.x:.2f}, y={self.y:.2f}, dir={self.direction}°)"
