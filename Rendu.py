import math
import keyboard
import time
import pygame


# Configuration des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0, 255)


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = 0  # Orientation en degrés (0 = droite, 90 = haut, 180 = gauche, 270 = bas)


    def afficher_position(self):
        print(f"Position actuelle : ({self.x}, {self.y}), Orientation : {self.orientation}°")

   
    def tourner(self, angle):
        """Tourne le robot d'un certain angle (en degrés)"""
        self.orientation = (self.orientation + angle) % 360
        print(f"Orientation actuelle : {self.orientation}°")

class Environment:
    def __init__(self, largeur, longueur, obstacles):
        self.largeur = largeur
        self.longueur = longueur
        self.obstacles = obstacles

    def est_valide_position(self, x, y):
        """Vérifie si une position est valide (pas d'obstacle, pas hors des limites)"""
        if x < 0 or x >= self.largeur or y < 0 or y >= self.longueur:
            return False
        if (x, y) in self.obstacles:
            return False
        return True
    
    

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

class InterfaceGraphique: 
     def __init__(self, env_robot):
        pygame.init()
        self.screen_width = 500
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Robot dans l'environnement")
        self.env_robot = env_robot
        self.running = True

     def afficher(self):
        """Affiche l'environnement en 2D avec le robot et les obstacles"""
        self.screen.fill(WHITE)

        # Dessiner les obstacles
        for (obstacle_x, obstacle_y) in self.env_robot.environment.obstacles:
            pygame.draw.rect(self.screen, RED, (obstacle_x * 50, obstacle_y * 50, 50, 50))

        # Dessiner le robot
        robot = self.env_robot.robot
        center_x = robot.x * 50 + 25
        center_y = robot.y * 50 + 25
        pygame.draw.circle(self.screen, BLUE, (center_x, center_y), 10)

        # Dessiner la direction du robot
        direction_x = center_x + 20 * math.cos(math.radians(robot.orientation))
        direction_y = center_y - 20 * math.sin(math.radians(robot.orientation))
        pygame.draw.line(self.screen, BLACK, (center_x, center_y), (direction_x, direction_y), 3)

        pygame.display.flip()

     def run(self):
            """Boucle principale de l'interface graphique"""
            print("Commandes :")
            print(" - Flèches directionnelles pour avancer/reculer")
            print(" - Flèche gauche pour tourner à gauche")
            print(" - Flèche droite pour tourner à droite")
            print(" - 'q' pour quitter")

            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                # Vérifier les entrées clavier
                if keyboard.is_pressed("down"):
                    self.env_robot.deplacer_robot(-1)
                    time.sleep(0.2)
                elif keyboard.is_pressed("up"):
                    self.env_robot.deplacer_robot(1)
                    time.sleep(0.2)
                elif keyboard.is_pressed("left"):
                    self.env_robot.tourner_robot(45)
                    time.sleep(0.2)
                elif keyboard.is_pressed("right"):
                    self.env_robot.tourner_robot(-45)
                    time.sleep(0.2)
                elif keyboard.is_pressed("q"):
                    print("Fin du programme.")
                    self.running = False

                # Mise à jour de l'affichage
                self.afficher()

            pygame.quit()
   

if __name__ == "__main__":
    # Initialisation du robot et de l'environnement
    robot = Robot()
    environment = Environment(10, 10, [(2, 2), (4, 4)])  # Exemple d'obstacles
    controller = EnvRobot(robot, environment)

    # Lancer l'interface graphique
    interface = InterfaceGraphique(controller)
    interface.run()