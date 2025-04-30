import time
from time import pi

class adapterVirtuel:
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.obstcales = obstcales 
        self.angle = 0
        self.distance = 0
        self.derniere_maj= time.time()
        
        if robot:
            self.ecart_roue=robot.ecart_roue
            self.rayon_robot= robot.rayon
            self.rayon_roue= robot.taille_roue /2
            
    
    def difinir_vitesse(self,v_gauche, v_droite):
        if self.robot:
            self.robot.set_vitesses(v_gauche,v_droite)
        self.derniere_maj=time.time()
        
    def get_dt(self):
        current_time=time.time()
        dt=current_time=self.derniere_maj
        self.derniere_maj=current_time
        return dt
    
    def update(self):
        self.last_update = time.time()
        
    def avancer(self):
        dt=self.get_dt()
        self.robot.avancer(dt)
        self.update()
        
    def tourner(self):
        dt=self.get_dt()
        self.robot.tourner(dt)
        self.update()
    
    def dist_parcourue(self):
        dt=self.get_dt()
        vit_moyenne=(self.robot.vitesse_g+self.robot.vitesse_d)/2
        dist=vit_moyenne * dt
        self.distance+=dist
        return self.distance
    
    def get_ang_parcourue(self):
        dt=self.get_dt()
        dt_vitesse=self.robot.vitesse_d-self.robot.vitesse_g
        angle=(dt_vitesse/self.distance) * dt
        self.angle+=angle
        return math.degrees(self.angle) 
        
           
    
        
        
        
        
        
            
        