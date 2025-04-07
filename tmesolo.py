import time
import math
from Model.arene import Arene
from Model.robot import Robot
from Model.obstacle import Obstacle
#je cree l'arene, les obstacles et le robot directement pour ne pas avoir a les creer pour chaque fonction
arene1=Arene(largeur=900, hauteur=800)
obstacle1 = Obstacle(x=450, y=400, largeur=150, hauteur=100)
obstacle2 = Obstacle(x=450, y=10, largeur=70, hauteur=160)
obstacle3 = Obstacle(x=450, y=790, largeur=70, hauteur=160)
arene1.ajouter_obstacle(obstacle1)
arene1.ajouter_obstacle(obstacle2)
arene1.ajouter_obstacle(obstacle3)
robot = Robot(x=10, y=10, orientation=0, vitesse_gauche=0, vitesse_droite=0, diametre_roue=20, distance_roues=40)
def q1_1():
    for i in range(100):
        arene1.mise_a_jour(0.1)
        time.sleep(0.1)
class StrategieDemiTour:
    def __init__(self, robot, arene):
        self.robot = robot
        self.arene = arene
        self.demi_tours = 0
        self.dist = 10 #si il est proche d'un mur ou d'un obstacle

    def proche(self):
        if self.robot.x > self.arene.largeur - self.dist or self.robot.x < self.dist: # si il est proche d'un mur
            return True
        for obstacle in self.arene.obstacles:
            distance = math.sqrt((self.robot.x - obstacle.x)*(self.robot.x - obstacle.x)+ (self.robot.y - obstacle.y)*(self.robot.y - obstacle.y)) #la distance euclidienne
            if distance < self.robot.rayon + obstacle.rayon + 5:
                return True
        return False
    
    def appliquer(self, delta_t):
        if self.demi_tours >= 10: #on s'arrete apres 10 demi-tours
            self.robot.vitesse_gauche = 0
            self.robot.vitesse_droite = 0
            return False
        if self.proche(): #on fait demi-tour si on est trp proche
            self.robot.orientation += math.pi  #on tourne de 180 degres
            self.demi_tours += 1
        self.robot.vitesse_gauche = 10 #ni proche d'un obstacle ni proche d'un mur on avance
        self.robot.vitesse_droite = 10
        return True
    
def q1_2():
    strategie1= StrategieDemiTour(robot, arene1)
    for i in range(300):
        if not strategie1.appliquer(0.1):
            print("fin de la strategie apres 10 demi-tours")
            break
        arene1.mise_a_jour(0.1)
        time.sleep(0.1)
if __name__ == "__main__":
    q1_1()
    q1_2()
