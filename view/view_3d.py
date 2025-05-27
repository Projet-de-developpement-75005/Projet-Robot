from ursina import *
import math

hauteur_o=10
hauteur_r=2

class View3D:
    def __init__(self,arene,robot):
        #inituialiser l'application ursina
        self.app=Ursina()
        self.arene=arene
        self.robot=robot
        
        window.title="Simulation 3D Robot"
        window.borderless=False
        window.fullscreen=False
        window.exut_botton.visible=True
        window.fps_compteur=True #activer l'affichage du nombre de fps
        window.color=color.gray
        
        largeur=arene.largeur
        hauteur=arene.hauteur
        
        self.sol=Entity(model='plane',texture='white_cube',scale=(largeur,1,hauteur),position=(largeur/2,0,hauteur/2),texture_scale=(largeur/10,hauteur/10),color=color.green)
        self.robot=Entity(model='cube',color=color.azure,scale=(robot.ecart_roue,hauteur_r,robot.taille_roue),position=(robot.pos_x,hauteur_r/2,robot.pos_y))
        self.obstacle_entities =[]
        for obs in arene.liste_obstacles:
            obj=Entity(model='cube',
                       color=color.purple
                       scale=(obs.larg,hauteur_o,obs.longueur),
                        position=(obs.x+obs.larg/2,hauteur_o/2,obs.y+obs.longueur/2))
            self.obstacle_entities.append(obj)
            
        self.camera=EditorCamera(position=(largeur/2,50,hauteur/2))
        #pour cacher les elements d'interface par defaut d'Ursina
        camera.ui.enabled=False
        
        self.label=Text(text='',origin=(0,18),background=True)
        
        class Input_handler(Entity):
            def __init__(self,parent_view):
                super().__init__()
                self.parent_view=parent_view
            
            def input(self,key):
                if key=='escape':
                    application.quit()
                
                
                
        self.input_handler=Input_handler(self)
    def update_affichage(self):
        self.robot.position=(self.robot.pos_x,hauteur_r/2,self.robot.pos_y)
        self.robot.rotationY=-math.degrees(self.robot.angle_orientation)#ursina tourne par defaut dans le sens horaire 
        
        self.label.text=f"Pos:({self.robot.pos_x :.1f},{self.robot.pos_y : .1f})\n"+ \
                        f"Vg :{self.robot.vitesse_g :.1f}, Vd:{self.robot.vitesse_d :.1f}"
                        
        self.app.step() #pour mettre a jour la scene

        