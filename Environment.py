import pygame

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

class Environment:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Simulation de Robot 🤖")


    