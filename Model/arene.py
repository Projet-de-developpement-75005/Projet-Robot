import math

class Obstacle:
    def __init__(self,x,y,larg,longueur):
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
        
        return (dx2 **2 +dy2 **2)<= rayon **2
    
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
        
    def gerer_collisions(self, robot):
        """
        Gère les collisions avec les obstacles.
        """
        for obstacle in self.liste_obstacles:
            collision = obstacle.collision(robot.pos_x,robot.pos_y,robot.rayon)
            if collision:
                print("Collision détectée!")
                robot.set_vitesses(0,0)
                dx = obstacle.x - robot.pos_x
                dy = obstacle.y - robot.pos_y
                angle_robot = robot.angle_orientation
                angle_obstacle = math.atan2(dy, dx)
                delta_angle = (angle_obstacle - angle_robot + math.pi) % (2 * math.pi) - math.pi

                if -math.pi / 2 <= delta_angle <= math.pi / 2:
                  robot.set_vitesses(-5,-5)  
                else:
                    robot.set_vitesses(5,5)

                break