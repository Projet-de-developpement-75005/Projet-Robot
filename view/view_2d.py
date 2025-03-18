import tkinter as tk
import math
from Model.arene import Arene

class View(tk.Tk):
    def _init_(self, arene):
        super()._init_()
        self.title("Simulation Robot")
        self.arene = arene
        # Pour être sûr que le canevas recouvre toute la fenêtre
        self.canvas = tk.Canvas(self, width=arene.largeur, height=arene.hauteur, bg="white")
        self.canvas.pack()

    def update_affichage(self, robot, trace_points=None):
        # Effacer l'affichage précédent
        self.canvas.delete("all")
        margin = 10
        # Dessiner les limites de l'arène
        self.canvas.create_rectangle(margin, margin, self.arene.largeur - margin, self.arene.hauteur - margin, outline="black")
        
        # Dessiner les obstacles
        for obs in self.arene.obstacles:
            self.canvas.create_rectangle(obs.x, obs.y, obs.x + obs.largeur, obs.y + obs.hauteur, fill="red")
        
        # Si une trajectoire est fournie, dessiner le trait en vert
        if trace_points and len(trace_points) > 1:
            coords = []
            for (x, y) in trace_points:
                coords.extend([x, y])
            self.canvas.create_line(*coords, fill="green", width=2)
        
        # Dessiner le robot sous forme de rectangle orienté
        # On définit une longueur et une largeur pour le châssis
        L = robot.distance_roues  # longueur approximative
        l = robot.distance_roues + robot.diametre_roue  # largeur approximative
        half_L = L / 2
        half_l = l / 2
        theta = robot.orientation
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        # Points du châssis dans le repère local
        points_local = [
            ( half_L, -half_l),
            ( half_L,  half_l),
            (-half_L,  half_l),
            (-half_L, -half_l)
        ]
        poly_points = []
        for (x_local, y_local) in points_local:
            x_global = robot.x + x_local * cos_t - y_local * sin_t
            y_global = robot.y + x_local * sin_t + y_local * cos_t
            poly_points.extend([x_global, y_global])
        self.canvas.create_polygon(poly_points, fill="blue")
        
        # Dessiner les roues
        dist = robot.distance_roues
        x_left = robot.x - (dist/2) * sin_t
        y_left = robot.y - (dist/2) * cos_t
        x_right = robot.x + (dist/2) * sin_t
        y_right = robot.y + (dist/2) * cos_t
        r = robot.diametre_roue / 2
        self.canvas.create_oval(x_left - r, y_left - r, x_left + r, y_left + r, fill="black")
        self.canvas.create_oval(x_right - r, y_right - r, x_right + r, y_right + r, fill="black")
        
        # Dessiner un repère de rotation sur chaque roue (ligne blanche)
        phi_left = getattr(robot, "angle_roue_gauche", 0)
        end_x_left = x_left + (r * math.sin(phi_left) * 0.9) * cos_t - (r * math.cos(phi_left) * 0.9) * sin_t
        end_y_left = y_left + (r * math.sin(phi_left) * 0.9) * sin_t + (r * math.cos(phi_left) * 0.9) * cos_t
        self.canvas.create_line(x_left, y_left, end_x_left, end_y_left, fill="white", width=2)
        phi_right = getattr(robot, "angle_roue_droite", 0)
        end_x_right = x_right + (r * math.sin(phi_right) * 0.9) * cos_t - (r * math.cos(phi_right) * 0.9) * sin_t
        end_y_right = y_right + (r * math.sin(phi_right) * 0.9) * sin_t + (r * math.cos(phi_right) * 0.9) * cos_t
        self.canvas.create_line(x_right, y_right, end_x_right, end_y_right, fill="white", width=2)
        
        self.update()