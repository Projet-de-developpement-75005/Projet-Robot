import tkinter as tk
import math

class View(tk.Tk):
    def __init__(self, arene, robot):
        super().__init__()
        self.title("Simulation Robot")
        self.arene = arene
        self.robot = robot
        self.canvas = tk.Canvas(self, width=arene.largeur, height=arene.hauteur, bg="white")
        self.canvas.pack()
        self.trace_points = []

    def update_affichage(self):
        self.canvas.delete("all")

        # Affichage de la bordure
        margin = 10
        self.canvas.create_rectangle(
            margin, margin,
            self.arene.largeur - margin,
            self.arene.hauteur - margin,
            outline="black"
        )

        # Obstacles
        for obs in self.arene.liste_obstacles:
            self.canvas.create_rectangle(obs.x, obs.y, obs.x + obs.larg, obs.y + obs.longueur, fill="red")

        # Tracer la trajectoire
        self.trace_points.append((self.robot.pos_x, self.robot.pos_y))
        if len(self.trace_points) > 1:
            coords = []
            for (x, y) in self.trace_points:
                coords.extend([x, y])
            self.canvas.create_line(*coords, fill="green", width=2)

        # Corps du robot en bleu
        L = self.robot.ecart_roue
        l = L + self.robot.taille_roue
        half_L = L / 2
        half_l = l / 2
        theta = self.robot.angle_orientation
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)

        # Coins du rectangle du robot
        points_local = [
            ( half_L, -half_l),
            ( half_L,  half_l),
            (-half_L,  half_l),
            (-half_L, -half_l)
        ]
        poly_points = []
        for (x_local, y_local) in points_local:
            x_global = self.robot.pos_x + x_local * cos_t - y_local * sin_t
            y_global = self.robot.pos_y + x_local * sin_t + y_local * cos_t
            poly_points.extend([x_global, y_global])

        self.canvas.create_polygon(poly_points, fill="blue")

        # Roues 
        vx = math.cos(theta)
        vy = math.sin(theta)
        px = -vy
        py = vx
        x_center = self.robot.pos_x
        y_center = self.robot.pos_y
        half_dist = self.robot.ecart_roue / 2
        r = self.robot.taille_roue / 2

        # Roue gauche
        x_left = x_center + px * (-half_dist)
        y_left = y_center + py * (-half_dist)
        self.canvas.create_oval(x_left - r, y_left - r, x_left + r, y_left + r, fill="black")

        # Roue droite
        x_right = x_center + px * (half_dist)
        y_right = y_center + py * (half_dist)
        self.canvas.create_oval(x_right - r, y_right - r, x_right + r, y_right + r, fill="black")

        self.update()