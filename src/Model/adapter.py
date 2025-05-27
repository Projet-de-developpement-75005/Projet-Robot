import math
import time 

class AdapterVirtuel:
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.obstacles = obstacles
        self.angle = 0
        self.derniere_maj= time.time()
        
        if robot:
            self.ecart_roue=robot.ecart_roue
            self.rayon_robot= robot.rayon
            self.rayon_roue= robot.taille_roue /2
            
    
    def definir_vitesse(self,v_gauche, v_droite):
        if self.robot:
            self.robot.set_vitesses(v_gauche,v_droite)
        self.derniere_maj=time.time()
        
    def get_dt(self):
        current_time=time.time()
        dt=current_time -self.derniere_maj
        self.derniere_maj=current_time
        return dt
    
    def update(self):
        self.last_update = time.time()
        
    def avancer(self):
        dt=self.get_dt()
        self.robot.deplacement(dt)
        self.update()
        
    def tourner(self):
        dt=self.get_dt()
        self.robot.rotation(dt)
        self.update()
    
    
    def dist_parcourue(self):
        return self.robot.get_distance()

    def get_ang_parcourue(self):
        dt=self.get_dt()
        dt_vitesse=self.robot.vitesse_d-self.robot.vitesse_g
        angle=(dt_vitesse/self.robot.ecart_roue) * dt
        self.angle+=angle
        return math.degrees(self.angle) 
        
           
    
        
        
        
        
        
            
        