import tkinter as tk
import math
from Model.arene import Arene

class View(tk.Tk):
    def __init__(self, arene):
        super().__init__()
        self.title("Simulation Robot")
        self.arene = arene
        self.canvas = tk.Canvas(self, width=arene.largeur, height=arene.hauteur, bg="white")
        self.canvas.pack()

    def update_affichage(self, robot):
        self.canvas.delete("all")
        margin = 10
        self.canvas.create_rectangle(margin, margin, self.arene.largeur - margin, self.arene.hauteur - margin, outline="black")

        # Obstacles
        for obs in self.arene.obstacles:
            self.canvas.create_rectangle(obs.x, obs.y, obs.x + obs.largeur, obs.y + obs.hauteur, fill="red")

        #si le crayon est baisse on fait la trace bleue
        if robot.crayon_baisse and len(robot.trace) > 1:
            coords = []
            for (x, y) in robot.trace:
                coords.extend([x, y])
            self.canvas.create_line(*coords, fill="blue", width=2)

        # Corps du robot
        L = robot.distance_roues
        l = robot.distance_roues + robot.diametre_roue
        half_L = L / 2
        half_l = l / 2
        theta = robot.orientation
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)

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

        # Roues
        vx = math.cos(theta)
        vy = math.sin(theta)
        px = -vy
        py = vx
        x_center = robot.x
        y_center = robot.y
        half_dist = robot.distance_roues / 2
        r = robot.diametre_roue / 2

        x_left = x_center + px * (-half_dist)
        y_left = y_center + py * (-half_dist)
        x_right = x_center + px * (half_dist)
        y_right = y_center + py * (half_dist)

        self.canvas.create_oval(x_left - r, y_left - r, x_left + r, y_left + r, fill="black")
        self.canvas.create_oval(x_right - r, y_right - r, x_right + r, y_right + r, fill="black")

        # Repère (facultatif)
        phi_left = getattr(robot, "angle_roue_gauche", 0)
        end_x_left = x_left + r * math.cos(phi_left)
        end_y_left = y_left + r * math.sin(phi_left)

        phi_right = getattr(robot, "angle_roue_droite", 0)
        end_x_right = x_right + r * math.cos(phi_right)
        end_y_right = y_right + r * math.sin(phi_right)

        self.update()
