import math
import time

class Controller:
    def __init__(self,adapter):
        self.adapter=adapter
    
    def run_simulation(self, strategie, view=None):
        active = True

        print("Simulation démarrée !")
        strategie.start(self.adapter)

        while active:
            termine = strategie.update(self.adapter)
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
    
    def update(self,adapter):
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
            
    def update(self,adapter):
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
    def __init__(self,condition_fonction,action1,action2):
        self.condition_fonction=condition_fonction
        self.action1=action1
        self.action2=action2
        self.action_courante=None
        self.condition_evaluee=False
        
    def start(self,adapter):
        if self.condition_fonction(adapter):
            self.action_courante=self.action1
        else:
            self.action_courante = self.action2
        self.action_courante.start(adapter)
        self.condition_evaluee = True
        
    def update(self,adapter):       
        if self.action_courante:
            fini=self.action_courante.update(adapter)
            if fini:
                self.action_courante.stop(adapter)
                return True
        return False       
    
    def stop(self,adapter):
        if self.action_courante:
            self.action_courante.stop(adapter)
            
            
            
class StrategieSequentielle:
    def __init__(self,liste_etapes):
        self.etapes=liste_etapes
        self.position=0
        
    def start(self,adapter):
        if len(self.etapes) >0:
            self.position=0
            self.etapes[self.position].start(adapter)
            
            
    def update(self,adapter):
        if self.position <len(self.etapes):
            fini=self.etapes[self.position].update(adapter)
            if fini:
                self.etapes[self.position].stop(adapter)
                self.position+=1
                if self.position <len(self.etapes):
                    self.etapes[self.position].start(adapter)
                    

            
        return self.position >=len(self.etapes)
    
    
    def stop(self,adapter):
        if self.position <len(self.etapes):
            self.etapes[self.position].stop(adapter) 
        
        