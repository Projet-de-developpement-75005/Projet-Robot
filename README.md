class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def deplacer(self, direction):
        if direction == "haut":
            self.y += 1
        elif direction == "bas":
            self.y -= 1
        elif direction == "gauche":
            self.x -= 1
        elif direction == "droite":
            self.x += 1
        else:
            print("Direction non valide ! Utilisez 'haut', 'bas', 'gauche' ou 'droite'.")

    def afficher_position(self):
        print(f"Position actuelle : ({self.x}, {self.y})")

    def get_position(self):
        return self.x, self.y


class Environment:
    def __init__(self, largeur, longueur, obstacles):
        self.largeur = largeur
        self.longueur = longueur
        self.obstacles = obstacles

    def estValidePosition(self, x, y):
        if x < 0 or x >= self.largeur or y < 0 or y >= self.longueur:
            return False
        if (x, y) in self.obstacles:
            return False
        return True


class EnvRobot:
    def __init__(self, robot, environment):
        self.robot = robot
        self.environment = environment

    def deplacer_robot(self, direction):
        new_x, new_y = self.robot.x, self.robot.y
        if direction == "haut":
            new_y += 1
        elif direction == "bas":
            new_y -= 1
        elif direction == "gauche":
            new_x -= 1
        elif direction == "droite":
            new_x += 1

        if self.environment.estValidePosition(new_x, new_y):
            self.robot.x, self.robot.y = new_x, new_y
        else:
            print("Mouvement impossible : obstacle ou hors des limites.")


if __name__ == "__main__":
    # Crée un environnement avec des obstacles
    env = Environment(10, 10, [(2, 2), (3, 4), (5, 5)])

    # Initialise un robot
    robot = Robot()

    # Crée un contrôleur
    controller = EnvRobot(robot, env)

    # Mode interactif
    while True:
        robot.afficher_position()
        direction = input("Entrez une direction (haut, bas, gauche, droite) ou 'quit' pour arrêter : ").strip().lower()
        if direction == "quit":
            print("Fin du programme.")
            break
        controller.deplacer_robot(direction)
