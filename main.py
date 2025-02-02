

from Robot import Robot
from Environment import Environment
from Env_robot import EnvRobot
from Interface import InterfaceGraphique

if __name__ == "__main__":
    # Initialisation du robot et de l'environnement
    robot = Robot()
    environment = Environment(10, 10, [(2, 2), (4, 4)])  # Exemple d'obstacles
    controller = EnvRobot(robot, environment)

    # Lancer l'interface graphique
    interface = InterfaceGraphique(controller)
    interface.run()
