class Controller:
    def __init__(self, robot):
        self.robot = robot

    def appliquer_strategie(self, strategie):
        strategie.executer(self.robot)


class StrategieAvancer:
    def __init__(self, distance, vitesse):
        self.distance = distance
        self.vitesse = vitesse

    def executer(self, robot):
        robot.vitesse_gauche = self.vitesse
        robot.vitesse_droite = self.vitesse


class StrategieTourner:
    def __init__(self, angle, vitesse):
        self.angle = angle
        self.vitesse = vitesse

    def executer(self, robot):
        if self.angle > 0:
            robot.vitesse_gauche = -self.vitesse
            robot.vitesse_droite = self.vitesse
        else:
            robot.vitesse_gauche = self.vitesse
            robot.vitesse_droite = -self.vitesse


class StrategieSequentielle:
    def __init__(self):
        self.strategies = [
            StrategieAvancer(50, 10),
            StrategieTourner(90, 5),
            StrategieAvancer(50, 10),
            StrategieTourner(90, 5),
            StrategieAvancer(50, 10),
            StrategieTourner(90, 5),
            StrategieAvancer(50, 10),
            StrategieTourner(90, 5)
        ]

    def executer(self, robot):
        for strategie in self.strategies:
            strategie.executer(robot)


class CapteurDistance:
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.obstacles = obstacles

    def mesurer_distance(self):
        distances = [
            ((obstacle.x - self.robot.x)**2 + (obstacle.y - self.robot.y)**2)**0.5
            for obstacle in self.obstacles
        ]
        return min(distances) if distances else float('inf')
