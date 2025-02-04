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
        
    def afficher_infos(self, voiture, temps_ecoule):
        """Affiche les informations de vitesse et le temps écoulé en dessous des vitesses."""
        font = pygame.font.SysFont(None, 30)
    
        # Convertir le temps écoulé en format hh:mm:ss
        heures = int(temps_ecoule // 3600)
        minutes = int((temps_ecoule % 3600) // 60)
        secondes = int(temps_ecoule % 60)
        temps_formate = f"{heures:02d}:{minutes:02d}:{secondes:02d}"

        # Création des textes
        texte_vitesse_gauche = font.render(f"Vitesse Roue Gauche: {voiture.vitesse_roue_gauche}", True, NOIR)
        texte_vitesse_droite = font.render(f"Vitesse Roue Droite: {voiture.vitesse_roue_droite}", True, NOIR)
        texte_temps = font.render(f"Temps écoulé: {temps_formate}", True, NOIR)

        # Affichage des textes à gauche en haut
        self.fenetre.blit(texte_vitesse_gauche, (20, 20))
        self.fenetre.blit(texte_vitesse_droite, (20, 50))
        self.fenetre.blit(texte_temps, (20, 80))  # Temps écoulé affiché en dessous des vitesses  


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
    def rafraichir_ecran(self, voiture, obstacles, temps_ecoule):
        """Rafraîchit l'écran avec les nouvelles informations."""
        self.fenetre.fill(BLANC)  # Nettoyer l'écran
        self.dessiner_voiture(voiture)  # Dessiner la voiture
        self.dessiner_obstacles(obstacles)  # Dessiner les obstacles
        self.afficher_infos(voiture, temps_ecoule)  # Afficher infos vitesse + temps
        pygame.display.flip()  # Mettre à jour l'affichage