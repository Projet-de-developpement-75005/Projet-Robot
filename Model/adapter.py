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

class Proxy_Reel:

	def __init__(self, robot):
		print("init")
		self.robot = robot
		self.dist_roue = self.robot.WHEEL_BASE_WIDTH
		self.rayon = self.robot.WHEEL_BASE_WIDTH / 2
		self.rayon_roue = self.robot.WHEEL_DIAMETER / 2
		self.circonf_roue = self.robot.WHEEL_CIRCUMFERENCE
		self.distance_parcourue = 0
		self.angle_parcouru = 0
		self.last_update = 0
		self.last_Ang = (0, 0)

		self.robot.offset_motor_encoder(self.robot._gpg.MOTOR_LEFT, self.robot.read_encoders()[0])
		self.robot.offset_motor_encoder(self.robot._gpg.MOTOR_RIGHT, self.robot.read_encoders()[1])

	def set_vitesse(self, dps1, dps2):
		print("set vitesse ", dps1, " ", dps2)
		self.robot.set_motor_dps(self.robot._gpg.MOTOR_LEFT, dps1)
		self.robot.set_motor_dps(self.robot._gpg.MOTOR_RIGHT, dps2)

	def update_distance(self):
		self.distance_parcourue = sum([i / 360 * self.circonf_roue for i in self.robot.get_motor_position()]) / 2

	def reset_distance(self):
		self.distance_parcourue = 0

	def update_angle(self):
		ang1, ang2 = self.get_vitAng()
		now = time.time()
		self.angle_parcouru += (now - self.last_update) * (ang1 - ang2) * self.rayon / self.dist_roue * 180 / np.pi

	def reset_angle(self):
		self.robot.offset_motor_encoder(self.robot._gpg.MOTOR_LEFT, self.robot.read_encoders()[0])
		self.robot.offset_motor_encoder(self.robot._gpg.MOTOR_RIGHT, self.robot.read_encoders()[1])
		ang = self.robot.get_motor_position()
		print("reset_angle", ang[0], ang[1])
		self.angle_parcouru = 0

	def get_capteur_distance(self):
		return self.robot.get_distance()

	def get_vitAng(self):
		now = time.time()
		Ang = self.robot.get_motor_position()
		a1, a2 = np.subtract(Ang, self.last_Ang)
		a1 = a1 * (now - self.last_update)
		a2 = a2 * (now - self.last_update)
		return (a1, a2)

	def tourner(self, rps):
		print("tourner ", rps)
		delta = (self.dist_roue * np.abs(rps)) / self.rayon_roue / 2
		if rps > 0:
			self.set_vitesse(delta, -delta)
		else:
			self.set_vitesse(-delta, delta)

	def reset(self):
		self.reset_angle()
		self.reset_distance()

	def update(self):
		now = time.time()
		self.update_distance()
		self.update_angle()
		self.last_Ang = self.robot.get_motor_position()
		self.last_update = now
