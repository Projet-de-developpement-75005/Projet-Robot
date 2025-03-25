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
	
	def tourner(self, dps):
		delta = (self.dist_roue * np.abs(dps)) / self.rayon_roue / 2
		if dps > 0:
			self.set_vitesse(delta, -delta)
		else:
			self.set_vitesse(-delta, delta)
		self.update()

	def reset(self):
		self.reset_angle()
		self.reset_distance()

	def update(self):
		now = time.time()
		self.update_distance()
		self.update_angle()
		self.last_update = now

class Proxy_Virtuel:

	def __init__(self, robot, env):
		self.robot = robot
		self.env = env
		self.dist_roue = self.robot.dist_roue
		self.rayon = self.robot.rayon
		self.rayon_roue = self.robot.rayon_roue
		self.distance_parcourue = 0
		self.angle_parcouru = 0
		self.last_update = 0
		self.angle_depart = self.robot.theta

	def set_vitesse(self, dps1, dps2):
		self.robot.vitAngG = dps1 / 20
		self.robot.vitAngD = dps2 / 20
		self.update()

	def update_distance(self):
		now = time.time()
		if self.last_update == 0:
			self.last_update = now
		else:
			ang_g, ang_d = self.get_vitAng()
			delta = self.robot.rayon_roue * (now - self.last_update) * (ang_g + ang_d) / 2
			self.distance_parcourue += delta

	def reset_distance(self):
		self.distance_parcourue = 0

	def update_angle(self):
		now = time.time()
		if self.last_update == 0:
			self.last_update = now
		else:
			ang1, ang2 = self.get_vitAng()
			self.angle_parcouru += (now - self.last_update) * (ang1 - ang2) * self.rayon / self.dist_roue * 180 / np.pi

	def reset_angle(self):
		self.angle_parcouru = 0
		self.angle_depart = self.robot.theta

	def get_capteur_distance(self):
		return self.robot.get_distance(self.env)

	def get_vitAng(self):
		return self.robot.get_vitAng()