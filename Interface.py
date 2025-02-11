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


    def dessiner_voiture(self, robot):
        """Dessine le robot et ses roues."""
        self.canvas.delete("robot")

       # Calculer les coins du rectangle après rotation
        x, y, angle = robot.x, robot.y, math.radians(robot.angle)
        cos_a, sin_a = math.cos(angle), math.sin(angle)

        demi_longueur = VOITURE_LONGUEUR / 2
        demi_largeur = VOITURE_LARGEUR / 2

         # Coins de la voiture avant rotation
        coins = [
            (-demi_longueur, -demi_largeur),
            (demi_longueur, -demi_largeur),
            (demi_longueur, demi_largeur),
            (-demi_longueur, demi_largeur),
        ]

        # Appliquer la rotation aux coins
        coins_rotates = [
            (x + cx * cos_a - cy * sin_a, y + cx * sin_a + cy * cos_a)
            for cx, cy in coins
        ]
    
    
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