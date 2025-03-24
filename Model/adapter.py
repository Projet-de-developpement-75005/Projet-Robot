from .robot import Robot

class Proxy_Virtuel:
	def __init__(self, robot, obstacles):
		self.robot = robot
		self.obstacles = obstacles
		self.dist_roue = robot.distance_roues
		self.rayon = robot.rayon
		self.rayon_roue = robot.diametre_roue / 2
		self.distance_parcourue = 0
		self.angle_parcouru = 0
		self.last_update = 0
		self.angle_depart = robot.orientation
  
    def set_vitesse(self, vitesse_gauche, vitesse_droite):
        self.robot.set_vitesses(vitesse_gauche, vitesse_droite)
    
    def update_distance(self):
        # On utilise le déplacement linéaire moyen pour simuler la distance parcourue
        rayon_roue = self.robot.diametre_roue / 2
        vitesse_gauche_lin = self.robot.vitesse_gauche * rayon_roue
        vitesse_droite_lin = self.robot.vitesse_droite * rayon_roue
        vitesse_moyenne = (vitesse_gauche_lin + vitesse_droite_lin) / 2
        self._distance += abs(vitesse_moyenne)
        
    def set_vitesse(self, vitesse_gauche, vitesse_droite):
        self.robot.set_vitesses(vitesse_gauche, vitesse_droite)
    
    def update_distance(self):
        # On utilise le déplacement linéaire moyen pour simuler la distance parcourue
        rayon_roue = self.robot.diametre_roue / 2
        vitesse_gauche_lin = self.robot.vitesse_gauche * rayon_roue
        vitesse_droite_lin = self.robot.vitesse_droite * rayon_roue
        vitesse_moyenne = (vitesse_gauche_lin + vitesse_droite_lin) / 2
        self._distance += abs(vitesse_moyenne)

	def reset_distance(self):
		self.distance_parcourue = 0
    


        
    



