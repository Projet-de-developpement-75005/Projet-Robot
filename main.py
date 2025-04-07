import time
from Model.arene import Arene
from Model.robot import Robot
from Model.adapter import Proxy_Virtuel, Proxy_Reel
from Model.obstacle import Obstacle
from view.view_3d import View3D
from controller.controller import (
    Controller,
    StrategieAvancer,
    StrategieTourner,
    StrategieConditionnelle,
    StrategieSequentielle,
    StrategieDemiTour
)

# 
mode = "virtuel"  
dt = 0.01  # intervalle de temps (en secondes)




# question 1
robot = Robot(x=50, y=700, orientation=0, vitesse_gauche=0, vitesse_droite=0, diametre_roue=20, distance_roues=40)
obstacle1 = Obstacle(x=470, y=50, largeur=70, hauteur=70)
obstacle2 = Obstacle(x=470, y=400, largeur=70, hauteur=70)
obstacle3 = Obstacle(x=470, y=700, largeur=70, hauteur=70)


adapter = Proxy_Virtuel(robot, obstacles=[obstacle1, obstacle2,obstacle3])
strategie = StrategieDemiTour(max_tours=10, distance=100, vitesse=50)
strategie.start(adapter)



from view.view_2d import View
arene = Arene(largeur=950, hauteur=800)
arene.ajouter_robot(robot)
arene.ajouter_obstacle(obstacle1)
arene.ajouter_obstacle(obstacle2)
arene.ajouter_obstacle(obstacle3)
view = View(arene)
#trace_points = []

    #strategie_sequentielle.start(adapter)

def update_simulation():
        termine = strategie.update(robot, 0.05)
        arene.mise_a_jour(0.05)
        view.update_affichage(robot)

        if not termine:
            view.after(50, update_simulation)
        else:
            print("strategie terminee.")

update_simulation()
view.mainloop()



