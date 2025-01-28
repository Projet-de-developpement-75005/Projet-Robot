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
    
    def afficher(self, screen, robot):
        """Affiche l'environnement en 2D avec le robot (point rouge) et sa direction (flèche noire)"""
        # Remplir le fond
        screen.fill(WHITE)

    # Dessiner les obstacles (carrés rouges)
        for (obstacle_x, obstacle_y) in self.obstacles:
            pygame.draw.rect(screen, RED, (obstacle_x * 50, obstacle_y * 50, 50, 50))

    # Dessiner le robot comme un point rouge
        center_x = robot.x * 50 + 25  # Centre du point rouge
        center_y = robot.y * 50 + 25
        pygame.draw.circle(screen, BLUE, (center_x, center_y), 10)  # Rayon de 5 pour un petit point

    # Dessiner la flèche indiquant la direction du robot
        direction_x = center_x + 20 * math.cos(math.radians(robot.orientation))
        direction_y = center_y - 20 * math.sin(math.radians(robot.orientation))
        pygame.draw.line(screen, BLACK, (center_x, center_y), (direction_x, direction_y), 3)

        pygame.display.flip()  # Met à jour l'affichage





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

   

    


if __name__ == "__main__":

    pygame.init()

    # Configuration de la fenêtre
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Robot dans l'environnement")


    print("Commandes :")
    print(" - Flèches directionnelles pour avancer/reculer")
    print(" - Flèche gauche pour tourner à gauche")
    print(" - Flèche droite pour tourner à droite")
    print(" - 'q' pour quitter")

    # Initialiser le robot et l'environnement
    robot = Robot()
    environment = Environment(10, 10, [(2, 2), (4, 4)])  # Exemple d'obstacles
    controller = EnvRobot(robot, environment)

    last_action_time = time.time()  # Temps de la dernière action
    debounce_time = 0.2  # Temps minimum entre deux actions (en secondes)

    
    # Boucle principale pour les commandes interactives
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Vérifier les entrées du clavier
        if keyboard.is_pressed("down"):
            controller.deplacer_robot(-1)  # Avance d'une unité dans la direction actuelle
            time.sleep(0.2)  # Pause pour éviter un mouvement trop rapide
        elif keyboard.is_pressed("up"):
            controller.deplacer_robot(1)  # Recule d'une unité dans la direction actuelle
            time.sleep(0.2)  # Pause pour éviter un mouvement trop rapide
        elif keyboard.is_pressed("left"):
            controller.tourner_robot(45)  # Tourne à gauche de 15°
            time.sleep(0.2)  # Pause pour éviter une rotation trop rapide
        elif keyboard.is_pressed("right"):
           controller.tourner_robot(-45)  # Tourne à droite de 15°
           time.sleep(0.2)  # Pause pour éviter une rotation trop rapide
        elif keyboard.is_pressed("q"):
            print("Fin du programme.")
            break 

        # Afficher l'environnement après chaque action
        environment.afficher(screen, robot)

pygame.quit()
