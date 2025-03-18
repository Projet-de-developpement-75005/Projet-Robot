
class Arene:
    def _init_(self, largeur, hauteur):
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
            self.robot.mise_a_jour(delta_t)
            for obstacle in self.obstacles:
                if obstacle.est_en_collision(self.robot.x, self.robot.y):
                    print("Collision détectée ! Le robot doit s'arrêter.")
                    self.robot.vitesse_gauche = 0
                    self.robot.vitesse_droite = 0



    
