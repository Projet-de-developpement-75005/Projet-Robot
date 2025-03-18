import tkinter as tk
from math import cos, sin, radians

class GUI:
    def __init__(self, arena, robot):
        """
        Interface graphique utilisant Tkinter pour afficher l'arène, le robot et ses traces.
        
        Args:
            arena (Arena): instance de l'arène.
            robot (Robot): instance du robot.
        """
        self.arena = arena
        self.robot = robot
        self.window = tk.Tk()
        self.window.title("Simulation Robot 2D")
        self.canvas = tk.Canvas(self.window, width=arena.width, height=arena.height, bg="white")
        self.canvas.pack()
        self.robot_item = None

    def draw(self):
        """Met à jour l'affichage : trace le parcours et dessine le robot."""
        # Dessiner la trace du robot
        if len(self.robot.trace) >= 2:
            # Supprimer l'ancienne trace
            self.canvas.delete("trace")
            points = []
            for (x, y) in self.robot.trace:
                points.extend([x, y])
            self.canvas.create_line(points, fill="blue", width=2, tags="trace")

        # Dessiner le robot comme un cercle
        if self.robot_item is not None:
            self.canvas.delete(self.robot_item)
        r = self.robot.rayon
        x, y = self.robot.x, self.robot.y
        self.robot_item = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")

        # Dessiner une ligne indiquant la direction du robot
        self.canvas.delete("dir")
        dx = r * 2 * cos(radians(self.robot.direction))
        dy = r * 2 * sin(radians(self.robot.direction))
        self.canvas.create_line(x, y, x + dx, y + dy, fill="black", width=2, tags="dir")
        self.canvas.update()

    def mainloop(self):
        """Lance la boucle principale de Tkinter."""
        self.window.mainloop()
