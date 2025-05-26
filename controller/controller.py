import math
import time

class Controller:
    def __init__(self,adapter):
        self.adapter=adapter
        
        
    def applique_strategie(self,strategie):
        """applique la strategie  en lancant start une fois ,appelant update
        et puis stop a la fin"""
        
        strategie.start(self.adapter)
        moment_precedent=time.time()
        
        for i in range(1000): #boucle de securite en cas de bug
            moment_actuel=time.time()
            delta_time=moment_actuel - moment_precedent 
            moment_precedent=moment_actuel
            
            termine=strategie.update(self.adapter,delta_time)
            if termine:
                break
            
        strategie.stop(self.adapter)
    def run_simulation(self, strategie, view=None):
        dernier_temps = time.time()
        active = True

        print("Simulation démarrée !")
        strategie.start(self.adapter)

        while active:
            temps_actuel = time.time()
            dt = temps_actuel - dernier_temps
            dernier_temps = temps_actuel

            termine = strategie.update(self.adapter, dt)
            if termine:
                active = False

            self.adapter.update()

            robot = self.adapter.robot
            print(f"Robot -> x:{robot.pos_x:.2f}, y:{robot.pos_y:.2f}, angle:{robot.angle_orientation:.2f}")

            if view:
                view.update_affichage()

            time.sleep(0.1)

        strategie.stop(self.adapter)
        print("Simulation terminée !")
        
class StrategieAvance:
    def __init__(self,distance_cible,vitesse):
        self.distance_cible=distance_cible
        self.vitesse=vitesse
        self.depart=0.0
        
    def start(self,adapter):
        self.depart=adapter.dist_parcourue()
        adapter.definir_vitesse(self.vitesse,self.vitesse)
    
    def update(self,adapter,dt):
        adapter.avancer()
        distance_actuelle=adapter.dist_parcourue()
        if(distance_actuelle -self.depart)>=self.distance_cible:
            return True
        return False
    
    def stop(self,adapter):
        adapter.definir_vitesse(0,0)
        


class StrategieTourner:
    def __init__(self,angle_deg,vitesse_rotation):
        self.angle_deg=angle_deg
        self.vitesse=vitesse_rotation
        self.angle_depart=None
        self.angle_cible=None
        
    def start(self,adapter):
        self.angle_depart=adapter.robot.angle_orientation
        self.angle_cible=self.angle_depart+math.radians(self.angle_deg)
        
        if self.angle_deg >0:
            adapter.definir_vitesse(-self.vitesse,self.vitesse)
            
        else:
            adapter.definir_vitesse(self.vitesse,-self.vitesse)
            
    def update(self,adapter,dt):
        adapter.tourner()
        angle_courant=adapter.robot.angle_orientation
        difference=self.angle_cible-angle_courant
        
        if(self.angle_deg >0 and difference<=0) or (self.angle_deg <0 and difference>=0):
            adapter.robot.angle_orientation=self.angle_cible
            
            return True
        return False
    
    def stop(self,adapter):
        adapter.definir_vitesse(0,0)
        
        
class StrategieConditionnelle:
    def __init__(self,action1,action2):
        self.action1=action1
        self.action2=action2
        self.etape=1
        
    def start(self,adapter):
        self.action1.start(adapter)
        
    def update(self,adapter,dt):       
        if self.etape==1:
            fini1=self.action1.update(adapter,dt)
            if fini1:
                self.action1.stop(adapter)
                self.etape=2
                self.action2.start(adapter)
                
        if self.etape==2:
            fini2=self.action2.update(adapter,dt)
            if fini2:
                self.action2.stop(adapter)
                return True
        
        return False
    
    def stop(self,adapter):
        if self.etape==1:
            self.action1.stop(adapter)
        else:
            self.action2.stop(adapter)
            
            
            
class StrategieSequentielle:
    def __init__(self,liste_etapes):
        self.etapes=liste_etapes
        self.position=0
        
    def start(self,adapter):
        if len(self.etapes) >0:
            self.position=0
            self.etapes[self.position].start(adapter)
            
            
    def update(self,adapter,dt):
        if self.position <len(self.etapes):
            fini=self.etapes[self.position].update(adapter,dt)
            if fini:
                self.etapes[self.position].stop(adapter)
                self.position+=1
                if self.position <len(self.etapes):
                    self.etapes[self.position].start(adapter)
                    

            
        return self.position >=len(self.etapes)
    
    
    def stop(self,adapter):
        if self.position <len(self.etapes):
            self.etapes[self.position].stop(adapter) 
        
        