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
