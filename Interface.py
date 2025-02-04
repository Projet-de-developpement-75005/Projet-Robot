import math
import pygame # type: ignore


# Configuration des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0, 255)
# Paramètres de la voiture
VOITURE_LONGUEUR = 60
VOITURE_LARGEUR = 30


class Interface:
    def _init_(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Simulation de Voiture avec Pygame")
        
    def afficher(self):
        """Affiche l'environnement en 2D avec le robot et les obstacles"""
        self.screen.fill(WHITE)

        # Dessiner les obstacles
        for (obstacle_x, obstacle_y) in self.env_robot.environment.obstacles:
            pygame.draw.rect(self.screen, RED, (obstacle_x * 50, obstacle_y * 50, 50, 50))

        # Dessiner le robot
        robot = self.env_robot.robot
        center_x = robot.x * 50 + 25
        center_y = robot.y * 50 + 25
        pygame.draw.circle(self.screen, BLUE, (center_x, center_y), 10)

        # Dessiner la direction du robot
        direction_x = center_x + 20 * math.cos(math.radians(robot.orientation))
        direction_y = center_y - 20 * math.sin(math.radians(robot.orientation))
        pygame.draw.line(self.screen, BLACK, (center_x, center_y), (direction_x, direction_y), 3)

        pygame.display.flip()
    def dessiner_voiture(self, voiture):
        """Dessine la voiture et ses roues."""
        # Rotation de la voiture
        voiture_surface = pygame.Surface((VOITURE_LONGUEUR, VOITURE_LARGEUR), pygame.SRCALPHA)
        voiture_surface.fill(ROUGE)
        voiture_surface_rotated = pygame.transform.rotate(voiture_surface, -voiture.angle)
        voiture_rect = voiture_surface_rotated.get_rect(center=(voiture.x, voiture.y))
        self.fenetre.blit(voiture_surface_rotated, voiture_rect)

        # Dessiner les roues
        roue_avant_gauche = (
            voiture.x + math.cos(math.radians(voiture.angle + 90)) * VOITURE_LARGEUR // 2,
            voiture.y + math.sin(math.radians(voiture.angle + 90)) * VOITURE_LARGEUR // 2,
        )
        roue_avant_droite = (
            voiture.x + math.cos(math.radians(voiture.angle - 90)) * VOITURE_LARGEUR // 2,
            voiture.y + math.sin(math.radians(voiture.angle - 90)) * VOITURE_LARGEUR // 2,
        )
        pygame.draw.circle(self.fenetre, BLEU, (int(roue_avant_gauche[0]), int(roue_avant_gauche[1])), 5)
        pygame.draw.circle(self.fenetre, BLEU, (int(roue_avant_droite[0]), int(roue_avant_droite[1])), 5)
    
    
    def dessiner_obstacles(self, obstacles):
        """Dessine les obstacles."""
        for obstacle in obstacles:
            pygame.draw.rect(self.fenetre, NOIR, obstacle)
