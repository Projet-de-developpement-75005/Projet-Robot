from Model.robot import Robot
from Model.arene import Arene,Obstacle
from Model.adapter import AdapterVirtuel
from controller.controller import Controller, StrategieSequentielle, StrategieAvance, StrategieTourner
from view.view_2d import View

robot = Robot(pos_x=300, pos_y=300, angle_orientaion=0, vitesse_g=0, vitesse_d=0, taille_roue=10, ecart_roue=40, rayon=20, distance=0)
arene = Arene(largeur=600, hauteur=600)
obstacle1=Obstacle(x=300,y=200,larg=50,longueur=50)
obstacle2=Obstacle(x=100,y=40,larg=50,longueur=50)
arene.ajout_obstacles(obstacle1)
arene.ajout_obstacles(obstacle2)
adapter = AdapterVirtuel(robot, arene.liste_obstacles)

# Stratégie de dessin d'un carré
strategie = StrategieSequentielle([
    StrategieAvance(distance_cible=100, vitesse=50),
    StrategieTourner(angle_deg=90, vitesse_rotation=30),
    StrategieAvance(distance_cible=100, vitesse=50),
    StrategieTourner(angle_deg=90, vitesse_rotation=30),
    StrategieAvance(distance_cible=100, vitesse=50),
    StrategieTourner(angle_deg=90, vitesse_rotation=30),
    StrategieAvance(distance_cible=100, vitesse=50),
    StrategieTourner(angle_deg=90, vitesse_rotation=30)
])

affichage = input("Voulez-vous activer l'affichage graphique ? (oui/non): ").strip().lower()
view = View(arene,robot) if affichage == "oui" else None

controller = Controller(adapter)
controller.run_simulation(strategie, view)
