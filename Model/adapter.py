from .robot import Robot

class Proxy_Virtuel:
    def __init__(self, robot, obstacles=None):
        self.robot = robot
        self.obstacles = obstacles if obstacles is not None else []
        self._distance = 0
        self._angle = 0

    def set_vitesse(self, vitesse_gauche, vitesse_droite):
        self.robot.set_vitesses(vitesse_gauche, vitesse_droite)


