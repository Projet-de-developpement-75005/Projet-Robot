import math

class Controller:
    def __init__(self, adapter):
        self.adapter = adapter

    def appliquer_strategie(self, strategie, dt):
        """
        Applique la stratégie en utilisant l'adapter.
        La stratégie est lancée via start, puis update est appelée en boucle
        jusqu'à ce que la stratégie indique qu'elle est terminée, puis stop est appelée.
        """
        strategie.start(self.adapter)
        while not strategie.update(self.adapter, dt):
            pass  # Vous pouvez ajouter un délai ici (ex: time.sleep(dt))
        strategie.stop(self.adapter)


class StrategieAvancer:
    def __init__(self, distance, vitesse):
        self.distance = distance
        self.vitesse = vitesse
        self.distance_initiale = None

    def start(self, adapter):
        self.distance_initiale = adapter.get_distance()
        adapter.set_vitesses(self.vitesse, self.vitesse)

    def update(self, adapter, dt):
        adapter.avancer(dt)
        if (adapter.get_distance() - self.distance_initiale) >= self.distance:
            return True  # La distance a été parcourue
        return False



import math

class StrategieTourner:
    def __init__(self, angle_degres, vitesse):
        """
        angle_degres : angle à tourner en degrés (positif = tourner à gauche, négatif = tourner à droite)
        vitesse : vitesse (ex. 5) pour la rotation
        """
        self.angle_degres = angle_degres
        self.vitesse = vitesse
        self.orientation_initiale = None
        self.orientation_cible = None

    def start(self, adapter):
        # On mémorise l'orientation de départ
        self.orientation_initiale = adapter.robot.orientation
        # On calcule l'orientation cible (en radians)
        self.orientation_cible = self.orientation_initiale + math.radians(self.angle_degres)
        
        # On règle les vitesses des roues pour tourner sur place
        if self.angle_degres > 0:
            # Tourne "à gauche" (roue gauche en arrière, roue droite en avant)
            adapter.set_vitesses(-self.vitesse, self.vitesse)
        else:
            # Tourne "à droite"
            adapter.set_vitesses(self.vitesse, -self.vitesse)

    def update(self, adapter, dt):
        # On fait tourner le robot pendant dt
        adapter.tourner(dt)
        
        # On récupère l'orientation actuelle
        current_orientation = adapter.robot.orientation
        # On calcule l'écart à l'orientation cible
        ecart = self.orientation_cible - current_orientation
        
        # Cas où l’on a atteint ou dépassé l'angle visé
        #  - Si angle_degres > 0, on surveille si ecart <= 0
        #  - Si angle_degres < 0, on surveille si ecart >= 0
        if (self.angle_degres > 0 and ecart <= 0) or (self.angle_degres < 0 and ecart >= 0):
            # On "verrouille" l'orientation sur la cible
            adapter.robot.orientation = self.orientation_cible
            return True
        return False

    def stop(self, adapter):
        # On arrête les roues
        adapter.set_vitesses(0, 0)



class StrategieConditionnelle:
    def __init__(self, strategie1, strategie2):
        """
        Combine deux stratégies : par exemple, avancer puis tourner.
        """
        self.strategie1 = strategie1
        self.strategie2 = strategie2
        self.phase = 1  # 1 pour la première stratégie, 2 pour la seconde

    def start(self, adapter):
        self.strategie1.start(adapter)

    def update(self, adapter, dt):
        if self.phase == 1:
            if self.strategie1.update(adapter, dt):
                self.strategie1.stop(adapter)
                self.phase = 2
                self.strategie2.start(adapter)
        if self.phase == 2:
            if self.strategie2.update(adapter, dt):
                self.strategie2.stop(adapter)
                return True  # Les deux stratégies sont terminées
        return False

    def stop(self, adapter):
        if self.phase == 1:
            self.strategie1.stop(adapter)
        else:
            self.strategie2.stop(adapter)


class StrategieSequentielle:
    def __init__(self, liste_strategies_conditionnelles):
        """
        liste_strategies_conditionnelles : liste de stratégies conditionnelles.
        Chaque élément (par exemple, avancer puis tourner) doit être exécuté
        entièrement avant de passer au suivant.
        """
        self.liste = liste_strategies_conditionnelles
        self.index = 0

    def start(self, adapter):
        if self.liste:
            self.index = 0
            self.liste[self.index].start(adapter)

    def update(self, adapter, dt):
        if self.index < len(self.liste):
            finished = self.liste[self.index].update(adapter, dt)
            if finished:
                self.liste[self.index].stop(adapter)
                self.index += 1
                if self.index < len(self.liste):
                    self.liste[self.index].start(adapter)
        return self.index >= len(self.liste)

    def stop(self, adapter):
        if self.index < len(self.liste):
            self.liste[self.index].stop(adapter)
