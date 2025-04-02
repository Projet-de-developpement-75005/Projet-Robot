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
    StrategieSequentielle
)

# === CHOIX DE MODE & AFFICHAGE ===
mode = "virtuel"  # ou "reel"
dt = 0.05  # intervalle de temps (en secondes)

# Demande du type d'affichage
print("Choisissez le mode d'affichage :")
print("1 - Affichage 2D")
print("2 - Affichage 3D")
choix_affichage = input("Entrez 1 ou 2 : ").strip()

if choix_affichage == "2":
    affichage = "3d"
elif choix_affichage == "1":
    affichage = "2d"
else:
    print("Erreur : il faut choisir 1 ou 2.")
    exit()  # Termine le programme proprement


# === INITIALISATION COMMUNE ===
robot = Robot(x=500, y=400, orientation=0, vitesse_gauche=0, vitesse_droite=0, diametre_roue=20, distance_roues=40)
obstacle = Obstacle(x=200, y=60, largeur=150, hauteur=100)
obstacle2 = Obstacle(x=400, y=350, largeur=70, hauteur=160)

if mode == "virtuel":
    adapter = Proxy_Virtuel(robot, obstacles=[obstacle, obstacle2])
else:
    adapter = Proxy_Reel(robot)

# Création des stratégies pour dessiner un carré
liste_strategies = []
for _ in range(4):
    strat_avancer = StrategieAvancer(distance=120, vitesse=50)
    strat_tourner = StrategieTourner(angle_degres=90, vitesse=10)
    strat_conditionnelle = StrategieConditionnelle(strat_avancer, strat_tourner)
    liste_strategies.append(strat_conditionnelle)

strategie_sequentielle = StrategieSequentielle(liste_strategies)
controller = Controller(adapter)

# === MODE VIRTUEL AVEC AFFICHAGE 2D ===
if mode == "virtuel" and affichage == "2d":
    from view.view_2d import View
    arene = Arene(largeur=950, hauteur=800)
    arene.ajouter_robot(robot)
    arene.ajouter_obstacle(obstacle)
    arene.ajouter_obstacle(obstacle2)
    view = View(arene)
    trace_points = []

    strategie_sequentielle.start(adapter)

    def update_simulation():
        finished = strategie_sequentielle.update(adapter, dt)
        arene.mise_a_jour(dt)
        trace_points.append((robot.x, robot.y))
        view.update_affichage(robot, trace_points)

        if not finished:
            view.after(int(dt * 1000), update_simulation)
        else:
            strategie_sequentielle.stop(adapter)
            print("Stratégie terminée, le robot a dessiné un carré.")

    update_simulation()
    view.mainloop()

# === MODE VIRTUEL AVEC AFFICHAGE 3D ===
elif mode == "virtuel" and affichage == "3d":
    
    arene = Arene(largeur=950, hauteur=800)
    arene.ajouter_robot(robot)
    arene.ajouter_obstacle(obstacle)
    arene.ajouter_obstacle(obstacle2)
    view3d = View3D(arene, robot)
    view3d.run_simulation(controller, strategie_sequentielle, dt)

# === MODE REEL ===
elif mode == "reel":
    controller.appliquer_strategie(strategie_sequentielle, dt)
    print("Stratégie terminée.")
