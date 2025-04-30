import math

class Obstacle:
    def __init_(self,x,y,larg,longueur):
        self.x=x
        self.y=y
        self.larg=larg
        self.longueur=longueur
        
    def collision(self,rx,ry,rayon):
        """detecte si le robot touche un certain obtacke"""
        cx = self.x + self.larg/2
        cy = self.y + self.longueur/2
        
        dx=abs(rx-cx)- self.larg/2
        dy=abs(ry-cy)- self.longueur/2
        
        dx2=max(dx,0)
        dy2=max(dy,0)
        
        return (dx **2 +dy **2)<= rayon **2
    
class Arene:
    def __init__(self,largeur, hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
        self.liste_obstacles=[]
        self.robot_actuel=None
        
    
    def placer_robot(self,robot):
        self.robot_actuel=robot
        
    def ajout_obstacles(self, obstacle):
        self.liste_obstacles.append(obstacle)
        
    def mouvement(self,dt):
        if self.robot_actuel:
            vitesse_moyenne=(self.robot_actuel.vitesse_d + self.robot_actuel.vitesse_g)/ 2.0
            changement_angle=(self.robot_actuel.vitesse_d -self.robot_actuel.vitesse_g) / self.robot_actuel.ecart_roue
            
            new_x=self.robot_actuel.pos_x +vitesse_moyenne*dt*math.cos(self.robot_actuel.angle_orientaion)
            new_y=self.robot_actuel.pos_y +vitesse_moyenne*dt*math.sin(self.robot_actuel.angle_orientaion)
            
            new_angle=self.robot_actuel.angle_orientaion+changement_angle
            
            i=0
            while i<len(self.liste_obstacles) and not self.liste_obstacles[i].collision(new_x,new_y,self.robot.rayon):
                i+=1
                if i<len(self.liste_obstacles):
                    print("collision evitée !")
                    self.robot.vitesse_g=self.vitesse_d=0
                else:
                    self.robot.pos_x, self.robot.pos_y=new_x,  new_y
                    self.robot.angle_orientaion += (self.robot.vitesse_d-self.robot.vitesse_g) /self.robot.ecart_roue
            
            
            