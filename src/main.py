from Model.robot import Robot
from Model.arene import Arene,Obstacle
from Model.adapter import AdapterVirtuel
from controller.controller import Controller, StrategieSequentielle, StrategieAvance, StrategieTourner, StrategieConditionnelle
from view.view_2d import View
from view.view_3d import View3D

robot = Robot(pos_x=300, pos_y=300, angle_orientation=0, vitesse_g=0, vitesse_d=0, taille_roue=20, ecart_roue=40)
arene = Arene(largeur=600, hauteur=600)
obstacle1=Obstacle(x=380,y=200,larg=50,longueur=50)
obstacle2=Obstacle(x=100,y=40,larg=50,longueur=50)
arene.ajout_obstacles(obstacle1)
arene.ajout_obstacles(obstacle2)
adapter = AdapterVirtuel(robot, arene.liste_obstacles)

#si le robot a parcouru moins de 1m, on avance 50 ; sinon on tourne 90°
def condition_initiale(adapter):
    return adapter.dist_parcourue() < 100

conditionnelle = StrategieConditionnelle(
    condition_fonction=condition_initiale,
    action1=StrategieAvance(distance_cible=90, vitesse=50),
    action2=StrategieTourner(angle_deg=90, vitesse_rotation=50)
)
strategie = StrategieSequentielle([
    conditionnelle,
    StrategieTourner(90, 50),
    StrategieAvance(100, 50),
    StrategieTourner(90, 50),
    StrategieAvance(100, 50),
    StrategieTourner(90, 50),
    StrategieAvance(100, 50)
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
