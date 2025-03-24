import time
import numpy as np 

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
		rayon_roue = self.robot.diametre_roue / 2
		vitesse_gauche_lin = self.robot.vitesse_gauche * rayon_roue
		vitesse_droite_lin = self.robot.vitesse_droite * rayon_roue
		vitesse_moyenne = (vitesse_gauche_lin + vitesse_droite_lin) / 2
		self.distance_parcourue += abs(vitesse_moyenne)

	def reset_distance(self):
		self.distance_parcourue = 0

	def reset_angle(self):
		self.angle_parcouru = 0
		self.angle_depart = self.robot.orientation

	def update_angle(self):
		now = time.time()
		if self.last_update == 0:
			self.last_update = now
		else:
			ang1, ang2 = self.get_vitAng()
			self.angle_parcouru += (now - self.last_update) * (ang1 - ang2) * self.rayon / self.dist_roue * 180 / np.pi

	def get_capteur_distance(self):
		return self.robot.capteur_distance(self.obstacles)

	def get_vitAng(self):
		return self.robot.get_vitesses_angulaires()

