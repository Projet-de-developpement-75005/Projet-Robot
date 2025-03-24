from .robot import Robot

class Proxy_Virtuel:
    def __init__(self, robot, obstacles=None):
        self.robot = robot
        self.obstacles = obstacles if obstacles is not None else []
        self._distance = 0
        self._angle = 0


