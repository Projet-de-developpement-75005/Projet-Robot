from math import cos, sin, radians, sqrt
from Model.update_model import check_collision
from Model.robot import Robot

class Deplacement:
    def __init__(self, robot,arena):
        self.robot = robot
        self.arena = arena

    def deplacer(self, distance):
        """Fait avancer le robot dans la direction actuelle."""
        new_x = self.robot.x + distance * cos(radians(self.robot.direction))
        new_y = self.robot.y + distance * sin(radians(self.robot.direction))

        for obstacle in self.arena.obstacles:
            if check_collision(Robot(new_x, new_y, self.robot.direction), obstacle):
                print(f"🚨 Collision anticipée avec {obstacle}, déplacement annulé !")
                return  # Annule le déplacement

        if 0 <= new_x <= self.arena.width and 0 <= new_y <= self.arena.height:
            self.robot.x = new_x
            self.robot.y = new_y
        else:
            print("🚧 Le robot atteint les limites de l'arène et s'arrête !")

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
    def __init__(self, robot, deplacement):
        self.robot = robot
        self.deplacement = deplacement

    def dessiner(self, longueur_cote):
        """Fait dessiner un carré au robot."""
        for _ in range(4):
            self.deplacement.deplacer(longueur_cote)
            self.deplacement.tourner(90)

class Controller:
    def __init__(self, robot, obstacles,arena):
        self.robot = robot
        self.obstacles = obstacles
        self.arena = arena
        self.deplacement = Deplacement(robot,arena)
        self.capteur = CapteurDistance(robot, obstacles)
        self.dessinateur = DessinerCarre(robot, self.deplacement)

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