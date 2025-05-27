from Model.robot import Robot
from Model.arene import Arene,Obstacle
from Model.adapter import AdapterVirtuel
from controller.controller import Controller, StrategieSequentielle, StrategieAvance, StrategieTourner, StrategieConditionnelle
from view.view_2d import View

robot = Robot(pos_x=300, pos_y=300, angle_orientation=0, vitesse_g=0, vitesse_d=0, taille_roue=10, ecart_roue=40)
arene = Arene(largeur=600, hauteur=600)
obstacle1=Obstacle(x=350,y=200,larg=50,longueur=50)
obstacle2=Obstacle(x=100,y=40,larg=50,longueur=50)
arene.ajout_obstacles(obstacle1)
arene.ajout_obstacles(obstacle2)
adapter = AdapterVirtuel(robot, arene.liste_obstacles)

# Exemple : si le robot a parcouru moins de 1m, on avance 50 ; sinon on tourne 90°
# (au lancement le robot n'a rien parcouru donc il avancera)
def condition_initiale(adapter):
    return adapter.dist_parcourue() < 100

# On veut voir visuellement la différence entre les deux choix
conditionnelle = StrategieConditionnelle(
    condition_fonction=condition_initiale,
    action1=StrategieAvance(distance_cible=50, vitesse=15),
    action2=StrategieTourner(angle_deg=90, vitesse_rotation=15)
)

# Enchaînement après la condition (un carré classique)
strategie = StrategieSequentielle([
    conditionnelle,
    StrategieAvance(100, 15),
    StrategieTourner(90, 15),
    StrategieAvance(100, 15),
    StrategieTourner(90, 15),
    StrategieAvance(100, 15),
    StrategieTourner(90, 15),
    StrategieAvance(100, 15),
    StrategieTourner(90, 15)
])

affichage = input("Voulez-vous activer l'affichage graphique ? (oui/non): ").strip().lower()
view = View(arene,robot) if affichage == "oui" else None

controller = Controller(adapter)
controller.run_simulation(strategie, view)
