import math
import pygame # type: ignore


# Configuration des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0, 255)
# Paramètres de la voiture
VOITURE_LONGUEUR = 60
VOITURE_LARGEUR = 30


class Interface:
    def _init_(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Simulation de Voiture avec Pygame")
        
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

