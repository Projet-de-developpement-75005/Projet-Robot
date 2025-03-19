import math

class Arene:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.obstacles = []
        self.robot = None

    def ajouter_robot(self, robot):
        self.robot = robot

    def ajouter_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def mise_a_jour(self, delta_t):
        if self.robot:
            # Calcul de la vitesse linéaire moyenne et du changement d'orientation
            average_speed = (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2.0
            delta_orientation = (self.robot.vitesse_droite - self.robot.vitesse_gauche) / self.robot.distance_roues

            # Calcul de la nouvelle position en fonction de l'orientation actuelle
            nouvelle_x = self.robot.x + average_speed * delta_t * math.cos(self.robot.orientation)
            nouvelle_y = self.robot.y + average_speed * delta_t * math.sin(self.robot.orientation)
            nouvelle_orientation = self.robot.orientation + delta_orientation * delta_t

            # Vérification des collisions pour la nouvelle position
            collision = False
            for obstacle in self.obstacles:
                if obstacle.est_en_collision(nouvelle_x, nouvelle_y, self.robot.rayon):
                    print("Collision détectée ! Le robot doit s'arrêter.")
                    collision = True
                    break

            if not collision:
                self.robot.x = nouvelle_x
                self.robot.y = nouvelle_y
                self.robot.orientation = nouvelle_orientation
            else:
                self.robot.vitesse_gauche = 0
                self.robot.vitesse_droite = 0
