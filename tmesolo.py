#exercice01:
from simulation.arene import Arene
from simulation.obstacle import Obstacle
from simulation.robot import Robot
from adapter import Proxy_Virtuel
from affichage.affichage2d import Affichage2D


# stratégie de demi tour:
class StrategieDemiTour:
    def __init__(self, proxy, arene, seuil_distance=50):
        self.proxy = proxy
        self.arene = arene
        self.seuil = seuil_distance
        self.nb_demi_tours = 0
        self.en_rotation = False
        self.angle_vise = 0

    def appliquer(self):
        if self.nb_demi_tours >= 10:
            self.proxy.set_vitesses(0, 0)
            return

        distance = self.proxy.capteur_distance(self.arene)

        if self.en_rotation:
            if abs(self.proxy.robot.angle - self.angle_vise) < 0.1:
                self.en_rotation = False
            else:
                self.proxy.tourner(1)
        elif distance < self.seuil:
            self.en_rotation = True
            self.nb_demi_tours += 1
            self.angle_vise = (self.proxy.robot.angle + 3.14) % (2 * 3.14)
            self.proxy.tourner(1)
        else:
            self.proxy.avancer(1)


#question1.1:
def q1_1_obstacles_alignés():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)

    rayon = 30
    obstacle_haut = Obstacle(x=largeur // 2, y=hauteur - 100, rayon=rayon)
    obstacle_milieu = Obstacle(x=largeur // 2, y=hauteur // 2, rayon=rayon)
    obstacle_bas = Obstacle(x=largeur // 2, y=100, rayon=rayon)

    arene.ajouter_obstacle(obstacle_haut)
    arene.ajouter_obstacle(obstacle_milieu)
    arene.ajouter_obstacle(obstacle_bas)

    robot = Robot(x=50, y=50, angle=0)
    proxy = Proxy_Virtuel(robot)
    arene.ajouter_robot(robot)

    affichage = Affichage2D(arene)
    affichage.run()

#question02:



def q1_2_demi_tour():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)

    obstacle = Obstacle(x=largeur // 2, y=hauteur // 2, rayon=40)
    arene.ajouter_obstacle(obstacle)

    robot = Robot(x=50, y=50, angle=0)
    proxy = Proxy_Virtuel(robot)
    arene.ajouter_robot(robot)

    strategie = StrategieDemiTour(proxy, arene)
    affichage = Affichage2D(arene)

    def boucle():
        arene.update()
        strategie.appliquer()


# test de la fonction :
if __name__ == "__main__":
    q1_2_demi_tour()  

#question03:

 # Attributs à ajouter dans __init__ de robot.py de la classe Robot:
self.trace_active = False
self.traces = []

# Méthode à ajouter dans la classe Robot :
def dessine(self, b: bool):
    """Active ou désactive le crayon (à ajouter dans robot.py)"""
    self.trace_active = b
    if b:
        self.traces = [(self.x, self.y)]
#commande à ajouter dans la méthode update(self, dt) de robot.py :
if self.trace_active:
    self.traces.append((self.x, self.y))


#Ajouter de la méthode  draw_robot() dans affichage2D.py:
if robot.trace_active and len(robot.traces) > 1:
    pygame.draw.lines(surface, (0, 0, 255), False, robot.traces, 2)


def q1_3_trace_robot():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)

    robot = Robot(x=50, y=300, angle=0)
    proxy = Proxy_Virtuel(robot)
    robot.dessine(True)  
    arene.ajouter_robot(robot)

    affichage = Affichage2D(arene)

    def boucle():
        arene.update()
        proxy.avancer(1)

    affichage.run(boucle)

#Question4:

#Attributs à ajouter dans __init__ de la classe Robot:
self.trace_active = False
self.traces = []
self.trace_couleur = (0, 0, 255)  



# Méthode à ajouter dans la classe Robot :
def bleu(self):
    self.trace_couleur = (0, 0, 255)

def rouge(self):
    self.trace_couleur = (255, 0, 0)

def dessine(self, b: bool):
    self.trace_active = b
    if b:
        self.traces = [(self.x, self.y, self.trace_couleur)]
 #commande à ajouter dans la méthode update(self, dt) de robot.py :
if self.trace_active:
    self.traces.append((self.x, self.y, self.trace_couleur))


#Ajouter ce bloc dans la méthode draw_robot() dans affichage2d.py:
if robot.trace_active and len(robot.traces) > 1:
  for i in range(len(robot.traces) - 1):
      x1, y1, c1 = robot.traces[i]
      x2, y2, c2 = robot.traces[i + 1]
      pygame.draw.line(surface, c1, (x1, y1), (x2, y2), 2)


def q1_4_trace_couleur():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)

    robot = Robot(x=50, y=300, angle=0)
    proxy = Proxy_Virtuel(robot)
    arene.ajouter_robot(robot)

    robot.bleu()         
    robot.dessine(True)   

    affichage = Affichage2D(arene)
    compteur = [0]

    def boucle():
        arene.update()
        proxy.avancer(1)

        compteur[0] += 1
        if compteur[0] == 200:
            robot.rouge()  
        if compteur[0] == 400:
            robot.bleu()   
    affichage.run(boucle)





#exercice02:
#question 01:


def q2_1_deux_robots():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)

    # Robot souris bleu
    souris = Robot(x=100, y=100, angle=0)
    proxy_souris = Proxy_Virtuel(souris)
    souris.dessine(True)
    souris.bleu()  
    arene.ajouter_robot(souris)

    # Robot chat rouge:
    chat = Robot(x=600, y=100, angle=3.14) 
    proxy_chat = Proxy_Virtuel(chat)
    chat.dessine(True)
    chat.rouge()  
    arene.ajouter_robot(chat)

    affichage = Affichage2D(arene)

    def boucle():
        arene.update()
        proxy_souris.avancer(1)
        proxy_chat.avancer(0.5)

    affichage.run(boucle)



#questions 02:

def q2_2_carre_souris_aller_retour_chat():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)


    souris = Robot(x=100, y=100, angle=0)
    souris.dessine(True)
    souris.bleu()
    proxy_souris = Proxy_Virtuel(souris)
    arene.ajouter_robot(souris)

    chat = Robot(x=700, y=300, angle=-1.57)
    chat.dessine(True)
    chat.rouge()
    proxy_chat = Proxy_Virtuel(chat)
    arene.ajouter_robot(chat)

    etape = [0]
    temps = [0]
    affichage = Affichage2D(arene)

    def boucle():
        arene.update()
        temps[0] += 1

        # Souris elle fait un carré 
        if etape[0] < 4:
            proxy_souris.avancer(1)
            if temps[0] % 100 == 0:
                proxy_souris.tourner(1)
                etape[0] += 1

        if (temps[0] // 200) % 2 == 0:
            proxy_chat.set_vitesses(0, -1)
        else:
            proxy_chat.set_vitesses(0, 1)

    affichage.run(boucle)

#question 03:

def q2_3_detection_catch():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)

    souris = Robot(x=300, y=300, angle=0)
    souris.dessine(True)
    souris.bleu()
    proxy_souris = Proxy_Virtuel(souris)
    arene.ajouter_robot(souris)

    chat = Robot(x=100, y=300, angle=0)
    chat.dessine(True)
    chat.rouge()
    proxy_chat = Proxy_Virtuel(chat)
    arene.ajouter_robot(chat)

    affichage = Affichage2D(arene)

    def boucle():
        arene.update()
        proxy_chat.avancer(1)


       
     #  ajouter dans robot.py:
        dx = chat.x - souris.x
        dy = chat.y - souris.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance < 2 * 60: 
            print("Attrapée !")
            exit()

    affichage.run(boucle)




#question04:

# ajout dans robot.py dans la classe Robot

def get_souris(self, robot_souris):
    from math import atan2, degrees, radians, pi

    dx = robot_souris.x - self.x
    dy = robot_souris.y - self.y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    angle_vers_souris = atan2(dy, dx)
    angle_relatif = angle_vers_souris - self.angle

    while angle_relatif > pi:
        angle_relatif -= 2 * pi
    while angle_relatif < -pi:
        angle_relatif += 2 * pi

    if -pi / 18 <= angle_relatif <= pi / 18:
        return distance, angle_relatif
    else:
        return None


def q2_4_capteur_souris():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)

    souris = Robot(x=400, y=300, angle=0)
    souris.dessine(True)
    souris.bleu()
    proxy_souris = Proxy_Virtuel(souris)
    arene.ajouter_robot(souris)

    chat = Robot(x=100, y=300, angle=0)
    chat.dessine(True)
    chat.rouge()
    proxy_chat = Proxy_Virtuel(chat)
    arene.ajouter_robot(chat)

    affichage = Affichage2D(arene)

    def boucle():
        arene.update()
        result = chat.get_souris(souris)
        if result:
            distance, angle = result
            print(f"Chat voit la souris ! Distance : {distance:.2f}, angle relatif : {angle:.2f} rad")
        else:
            print("Chat ne voit PAS la souris.")
        proxy_chat.avancer(0.5)

    affichage.run(boucle)


#question05:
#creation de la classe strategie:

class StrategieChasseur:
    """Stratégie de chasse qui utilise get_souris()"""
    def __init__(self, proxy_chat, robot_chat, robot_souris):
        self.proxy = proxy_chat
        self.chat = robot_chat
        self.souris = robot_souris

    def appliquer(self):
        result = self.chat.get_souris(self.souris)
        if result:
            _, angle = result
            if abs(angle) > 0.1:
                # Tourne vers la souris
                self.proxy.tourner(1 if angle > 0 else -1)
            else:
                # Avance vers la souris
                self.proxy.avancer(1)
        else:
            # Cherche la souris (rotation)
            self.proxy.tourner(1)



def q2_5_strategie_chasseur():
    largeur, hauteur = 800, 600
    arene = Arene(largeur, hauteur)

    souris = Robot(x=600, y=300, angle=0)
    souris.dessine(True)
    souris.bleu()
    proxy_souris = Proxy_Virtuel(souris)
    arene.ajouter_robot(souris)

    chat = Robot(x=100, y=300, angle=0)
    chat.dessine(True)
    chat.rouge()
    proxy_chat = Proxy_Virtuel(chat)
    arene.ajouter_robot(chat)

    strategie = StrategieChasseur(proxy_chat, chat, souris)

    affichage = Affichage2D(arene)

    def boucle():
        arene.update()
        proxy_souris.set_vitesses(0, 0)
        strategie.appliquer()
    #condition d'arret:
        dx = chat.x - souris.x
        dy = chat.y - souris.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance < 2 * 60:
            print("Chat a attrapé la souris !")
            exit()

    affichage.run(boucle)
