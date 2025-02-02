import math
import pygame
import time
import keyboard


# Configuration des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0, 255)


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