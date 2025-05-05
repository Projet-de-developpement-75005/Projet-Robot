import math
import time

class Robot:
    def __init__(self, pos_x, pos_y,angle_orientaion, vitesse_g, vitesse_d,taille_roue, ecart_roue, rayon, distance):
        
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.angle_orientaion=angle_orientaion
        self.vitesse_d=vitesse_d
        self.vitesse_g=vitesse_g
        self.taille_roue=taille_roue
        self.ecart_roue=ecart_roue
        self.rayon=ecart_roue / 2
        self.distance=0.0
        self.last_update=0
        
        
    def set_vitesses(self, new_vitesse_g, new_vitesse_d):
        
        self.vitesse_d=new_vitesse_d
        self.vitesse_g=new_vitesse_g
        print(f"Mise a jour des vitesses du moteur: G={new_vitesse_g:.2f}m/S, D={new_vitesse_d:.2f} m/s")        
        
    
    def get_distance(self):
        
        return self.distance
    
    def deplacement(self,dt):
        
        x_prec=self.pos_x
        y_prec=self.pos_y
        
        vitesse_moyenne=(self.vitesse_d+self.vitesse_g) / 2
        
        self.pos_x+=vitesse_moyenne * math.cos(self.angle_orientaion) *dt
        self.pos_y+=vitesse_moyenne * math.sin(self.angle_orientaion) * dt
        
        dx=self.pos_x - x_prec
        dy=self.pos_y - y_prec
        
        self.distance+=math.sqrt((dx**2)+(dy**2))
        
        print(f"Nouvelle coord x :{self.pos_x} et cood y :{self.pos_y} | la distance parcourue est :{self.distance: .3f}m")
        

    
    def rotation(self,dt):
        
        if self.vitesse_d != self.vitesse_g:
            delta_angle=(self.vitesse_d - self.vitesse_g)/self.distance *dt
            self.angle_orientaion+=delta_angle
            self.angle_orientaion %= (2*math.pi) #normalisation entre 0 et 2pi
            print(f"Rotation : Angle={math.degrees(self.angle_orientaion):.1f}")#convertit des angles exprimé en radians en degré
        
        
    def update(self):
        self.last_update = time.time()
        
        
        
        
        
        
        
        