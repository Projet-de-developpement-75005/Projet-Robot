import tkinter as tk
import math

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

    def afficher_infos(self, robot, temps_ecoule):
        """Affiche les informations de vitesse et le temps écoulé."""
        heures = int(temps_ecoule // 3600)
        minutes = int((temps_ecoule % 3600) // 60)
        secondes = int(temps_ecoule % 60)
        temps_formate = f"{heures:02d}:{minutes:02d}:{secondes:02d}"

        texte_vitesse_gauche = f"Vitesse Roue Gauche: {robot.vitesse_roue_gauche}"
        texte_vitesse_droite = f"Vitesse Roue Droite: {robot.vitesse_roue_droite}"
        texte_temps = f"Temps écoulé: {temps_formate}"

        self.canvas.create_text(20, 20, anchor="nw", text=texte_vitesse_gauche, fill=NOIR)
        self.canvas.create_text(20, 50, anchor="nw", text=texte_vitesse_droite, fill=NOIR)
        self.canvas.create_text(20, 80, anchor="nw", text=texte_temps, fill=NOIR)

    def dessiner_voiture(self, robot):
        """Dessine le robot avec des roues en tenant compte de la rotation."""
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

        # Dessiner le corps du robot
        self.canvas.create_polygon(
            [coord for point in coins_rotates for coord in point],
            fill=ROUGE, outline=NOIR, tags="robot"
        )

        # Position des roues par rapport au centre
        positions_roues = [
            (-demi_longueur + ROUE_LONGUEUR / 2, -demi_largeur - ROUE_LARGEUR / 2),  # Roue avant gauche
            (-demi_longueur + ROUE_LONGUEUR / 2, demi_largeur + ROUE_LARGEUR / 2),   # Roue avant droite
            (demi_longueur - ROUE_LONGUEUR / 2, -demi_largeur - ROUE_LARGEUR / 2),   # Roue arrière gauche
            (demi_longueur - ROUE_LONGUEUR / 2, demi_largeur + ROUE_LARGEUR / 2),    # Roue arrière droite
        ]

        # Dessiner les roues après rotation
        for dx, dy in positions_roues:
            roue_x = x + dx * cos_a - dy * sin_a
            roue_y = y + dx * sin_a + dy * cos_a
            self._dessiner_roue(roue_x, roue_y, angle)

    def _dessiner_roue(self, x, y, angle):
        """Dessine une roue avec la bonne orientation."""
        cos_a, sin_a = math.cos(angle), math.sin(angle)

        demi_l = ROUE_LONGUEUR / 2
        demi_w = ROUE_LARGEUR / 2

        # Coins de la roue avant rotation
        coins = [
            (-demi_l, -demi_w),
            (demi_l, -demi_w),
            (demi_l, demi_w),
            (-demi_l, demi_w),
        ]

        # Appliquer la rotation aux coins
        coins_rotates = [
            (x + cx * cos_a - cy * sin_a, y + cx * sin_a + cy * cos_a)
            for cx, cy in coins
        ]

        # Dessiner la roue
        self.canvas.create_polygon(
            [coord for point in coins_rotates for coord in point],
            fill=GRIS_FONCE, outline=NOIR, tags="robot"
        )


