import time
from Model.arene import Arene
from Model.robot import Robot
from controller.controller import Controller, StrategieAvancer, StrategieTourner, StrategieConditionnelle, StrategieSequentielle
from view.view_2d import View
from Model.adapter import Proxy_Virtuel, Proxy_Reel
from Model.obstacle import Obstacle

# Choisissez le mode : "virtuel" pour la simulation graphique ou "reel" pour un robot physique
mode = "virtuel"  # ou "reel"

# Intervalle de temps de mise à jour (en secondes)
dt = 0.05

# Création d'un robot (paramètres ajustables)
robot = Robot(x=500, y=400, orientation=0, vitesse_gauche=0, vitesse_droite=0, diametre_roue=20, distance_roues=40)
obstacle = Obstacle(x=200, y=60, largeur=150, hauteur=100)
obstacle2 = Obstacle(x=400, y=350, largeur=70, hauteur=160)





# Instanciation de l'adapter selon le mode choisi
if mode == "virtuel":
    # Pour le mode virtuel, on peut fournir une liste d'obstacles (ici vide)
    adapter = Proxy_Virtuel(robot, obstacles=[])
else:
    # En mode réel, instanciez Proxy_Reel avec votre robot physique
    adapter = Proxy_Reel(robot)

# Pour le mode virtuel, on crée une arène et une vue graphique
if mode == "virtuel":
    arene = Arene(largeur=950, hauteur=800)
    arene.ajouter_robot(robot)
    arene.ajouter_obstacle(obstacle)
    arene.ajouter_obstacle(obstacle2)
    view = View(arene)

# Liste pour enregistrer la trajectoire du robot (trace du carré)
trace_points = []

# Création d'une liste de stratégies conditionnelles pour dessiner un carré :
# Chaque élément correspond à une séquence : avancer d'une distance donnée, puis tourner de 90°.
liste_strategies = []
for _ in range(4):
    strat_avancer = StrategieAvancer(distance=120, vitesse=50)
    strat_tourner = StrategieTourner(angle_degres=90, vitesse=10)
    strat_conditionnelle = StrategieConditionnelle(strat_avancer, strat_tourner)
    liste_strategies.append(strat_conditionnelle)

# Création de la stratégie séquentielle qui enchaîne ces stratégies conditionnelles
strategie_sequentielle = StrategieSequentielle(liste_strategies)

# Instanciation du contrôleur avec l'adapter
controller = Controller(adapter)

if mode == "virtuel":
    # En mode virtuel, on lance la stratégie et on met à jour la simulation via Tkinter
    strategie_sequentielle.start(adapter)
    
    def update_simulation():
        finished = strategie_sequentielle.update(adapter, dt)
        # Mise à jour de l'arène (pour la gestion de collisions éventuelles)
        arene.mise_a_jour(dt)
        # Enregistrer la position actuelle du robot dans la trace
        trace_points.append((robot.x, robot.y))
        # Actualisation de l'affichage graphique en passant la trace
        view.update_affichage(robot, trace_points)
        
        if not finished:
            view.after(int(dt * 1000), update_simulation)
        else:
            strategie_sequentielle.stop(adapter)
            print("Stratégie terminée, le robot a dessiné un carré.")
    
    update_simulation()
    view.mainloop()
else:
    # En mode réel, on utilise le contrôleur pour appliquer la stratégie de manière bloquante
    controller.appliquer_strategie(strategie_sequentielle, dt)
    print("Stratégie terminée.")
