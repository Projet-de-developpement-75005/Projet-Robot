from Model.robot import Robot
from Model.arene import Arene,Obstacle
from Model.adapter import AdapterVirtuel
from controller.controller import Controller, StrategieSequentielle, StrategieAvance, StrategieTourner, StrategieConditionnelle
from view.view_2d import View
from view.view_3d import View3D

import random 

pos_x  = random.randrange(600)
pos_y  = random.randrange(600)
robot = Robot(pos_x, pos_y, angle_orientation=0, vitesse_g=0, vitesse_d=0, taille_roue=20, ecart_roue=40)
arene = Arene(largeur=600, hauteur=600)
obstacle1=Obstacle(x=380,y=200,larg=50,longueur=50)
obstacle2=Obstacle(x=100,y=40,larg=50,longueur=50)
#ajout dy myr
mur1=Obstacle(x=10,y=10,larg=600,longueur=10)
mur2=Obstacle(x=10,y=10,larg=10,longueur=600)
mur3=Obstacle(x=590,y=10,larg=10,longueur=600)
mur4=Obstacle(x=590,y=590,larg=600,longueur=10)

arene.ajout_obstacles(mur1)
arene.ajout_obstacles(mur2)
arene.ajout_obstacles(mur3)
arene.ajout_obstacles(mur4)
#arene.ajout_obstacles(obstacle1)
arene.ajout_obstacles(obstacle2)
adapter = AdapterVirtuel(robot, arene.liste_obstacles)

#si le robot a parcouru moins de 1m, on avance 50 ; sinon on tourne 90°
def condition_initiale(adapter):
    return adapter.dist_parcourue() < 100

conditionnelle = StrategieConditionnelle(
    condition_fonction=condition_initiale,
    action1=StrategieAvance(distance_cible=90, vitesse=50),
    action2=StrategieAvance(distance_cible=0,  vitesse=0) 
)
strategie = StrategieSequentielle([
    conditionnelle,
    StrategieAvance(distance_cible=100, vitesse=50),
    StrategieAvance(distance_cible=100, vitesse=50),
    StrategieAvance(distance_cible=100, vitesse=50),
    StrategieAvance(distance_cible=100, vitesse=50)
])

affichage = input("choisissez l'affichage(2D/3D:non): ").strip().lower()
if affichage == "2d":
    view = View(arene,robot) 
    
elif affichage == "3d":
    view=View3D(arene,robot)
    
else:
    view = None

controller = Controller(adapter,arene)
controller.run_simulation(strategie, view)
