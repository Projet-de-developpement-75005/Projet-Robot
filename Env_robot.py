import math 

class EnvRobot:
    def __init__(self, robot, environment):
        self.robot = robot
        self.environment = environment

    def deplacer_robot(self, distance):
        """Déplace le robot dans la direction actuelle si la position est valide"""
        x, y = self.robot.x, self.robot.y
        radian = math.radians(self.robot.orientation)
        new_x = x + round(distance * math.cos(radian))
        new_y = y - round(distance * math.sin(radian))

        if self.environment.est_valide_position(new_x, new_y):
            self.robot.x = new_x
            self.robot.y = new_y
            print(f"Position actuelle : ({new_x}, {new_y})")
        else:
            print("Mouvement impossible : obstacle ou hors des limites.")

    
    def tourner_robot(self, angle):
        """Tourne le robot d'un certain angle"""
        self.robot.tourner(angle)