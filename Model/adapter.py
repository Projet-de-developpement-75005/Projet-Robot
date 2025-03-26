import time
import numpy as np

class Proxy_Virtuel:
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.obstacles = obstacles
        self.dist_roue = robot.distance_roues
        self.rayon = robot.rayon
        self.rayon_roue = robot.diametre_roue / 2
        self.last_update = time.time()

    # On propose ici une interface commune aux stratégies :
    def set_vitesses(self, v1, v2):
        self.robot.set_vitesses(v1, v2)
    
    def avancer(self, dt):
        self.robot.avancer(dt)
        self.update()
    
    def tourner(self, dt):
        self.robot.tourner(dt)
        self.update()
    
    def get_distance(self):
        return self.robot.get_distance()
    
    def capteur_distance(self):
        return self.robot.capteur_distance(self.obstacles)
    
    def get_vitesses_angulaires(self):
        return self.robot.get_vitesses_angulaires()
    
    def update(self):
        self.last_update = time.time()


class Proxy_Reel:
    def __init__(self, robot):
        # Ici, on suppose que le robot réel possède certains attributs (sinon adaptez)
        self.robot = robot
        self.dist_roue = getattr(robot, "WHEEL_BASE_WIDTH", robot.distance_roues)
        self.rayon = self.dist_roue / 2
        self.rayon_roue = getattr(robot, "WHEEL_DIAMETER", robot.diametre_roue) / 2
        self.last_update = time.time()

    def set_vitesses(self, v1, v2):
        # Pour un robot réel, on envoie directement la commande aux moteurs
        self.robot.set_motor_dps(self.robot._gpg.MOTOR_LEFT, v1)
        self.robot.set_motor_dps(self.robot._gpg.MOTOR_RIGHT, v2)
    
    def avancer(self, dt):
        # Dans le cas réel, on suppose que la commande est envoyée et on attend dt
        time.sleep(dt)
        self.update()
    
    def tourner(self, dt):
        time.sleep(dt)
        self.update()
    
    def get_distance(self):
        return self.robot.get_distance()  # Adaptez si vous avez un autre moyen de mesurer la distance
    
    def capteur_distance(self):
        return self.robot.get_distance()  # Remplacez par la lecture d'un capteur réel si nécessaire
    
    def get_vitesses_angulaires(self):
        return self.robot.get_vitesses_angulaires()
    
    def update(self):
        self.last_update = time.time()
