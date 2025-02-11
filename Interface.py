import math
import tkinter as tk


# Configuration des couleurs
NOIR = "#000000"
ROUGE = "#FF0000"
GRIS_FONCE = "#333333"
# Paramètres de la voiture
VOITURE_LONGUEUR = 60
VOITURE_LARGEUR = 30
ROUE_LARGEUR = 6
ROUE_LONGUEUR = 12


class Interface:
    def __init__(self, canvas, largeur, hauteur):
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        
    def afficher_infos(self, voiture, temps_ecoule):
        """Affiche les informations de vitesse et le temps écoulé en dessous des vitesses."""
        
    
        # Convertir le temps écoulé en format hh:mm:ss
        heures = int(temps_ecoule // 3600)
        minutes = int((temps_ecoule % 3600) // 60)
        secondes = int(temps_ecoule % 60)
        temps_formate = f"{heures:02d}:{minutes:02d}:{secondes:02d}"

        # Création des textes
        texte_vitesse_gauche = f"Vitesse Roue Gauche: {robot.vitesse_roue_gauche}"
        texte_vitesse_droite = f"Vitesse Roue Droite: {robot.vitesse_roue_droite}"
        texte_temps = f"Temps écoulé: {temps_formate}"

        # Affichage des textes à gauche en haut
        self.canvas.create_text(20, 20, anchor="nw", text=texte_vitesse_gauche, fill=NOIR)
        self.canvas.create_text(20, 50, anchor="nw", text=texte_vitesse_droite, fill=NOIR)
        self.canvas.create_text(20, 80, anchor="nw", text=texte_temps, fill=NOIR)


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