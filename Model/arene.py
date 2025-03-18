<<<<<<< HEAD
class Arene:
    def _init_(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.obstacles = []
        self.robot = None

    






    
=======
class Arena:
    def __init__(self, width=400, height=400, scale=1):
        """
        Initialise l'arène avec ses dimensions et un facteur de mise à l'échelle.
        """
        self.width = width
        self.height = height
        self.scale = scale
        self.objets = []  # On pourra ajouter des obstacles ou autres objets

    def add_object(self, obj):
        """Ajoute un objet à l'arène."""
        self.objets.append(obj)
>>>>>>> 4a5f64ca772eada80f389441d7f800450aff36f7

