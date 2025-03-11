from math import cos, sin, radians, sqrt

class Deplacement:
    def __init__(self, robot):
        self.robot = robot

    def deplacer(self, distance):
        """Fait avancer le robot dans la direction actuelle."""
        self.robot.x += distance * cos(radians(self.robot.direction))
        self.robot.y += distance * sin(radians(self.robot.direction))

    def tourner(self, angle):
        """Fait tourner le robot."""
        self.robot.direction = (self.robot.direction + angle) % 360


class CapteurDistance:
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.obstacles = obstacles

    def obtenir_distance(self):
        """Retourne la distance entre le robot et l'obstacle le plus proche."""
        distance_min = float('inf')
        for obstacle in self.obstacles:
            distance = sqrt((self.robot.x - obstacle.x) ** 2 + (self.robot.y - obstacle.y) ** 2)
            distance_min = min(distance_min, distance)
        return distance_min


class DessinerCarre:
    def __init__(self, robot):
        self.robot = robot

    def dessiner(self, longueur_cote):
        """Fait dessiner un carré au robot."""
        for _ in range(4):
            self.robot.move(longueur_cote)
            self.robot.rotate(90)


class Controller:
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.obstacles = obstacles
        self.deplacement = Deplacement(robot)
        self.capteur = CapteurDistance(robot, obstacles)
        self.dessinateur = DessinerCarre(robot)

    def deplacer_robot(self, distance):
        """Déplace le robot."""
        self.deplacement.deplacer(distance)

    def tourner_robot(self, angle):
        """Fait tourner le robot."""
        self.deplacement.tourner(angle)

    def verifier_distance(self):
        """Retourne la distance entre le robot et l'obstacle."""
        return self.capteur.obtenir_distance()

    def dessiner_carre(self, longueur_cote):
        """Fait dessiner un carré au robot."""
        self.dessinateur.dessiner(longueur_cote)
