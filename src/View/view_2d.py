import tkinter as tk
import time
from update_affichage import update_affichage

class View2D:
    def __init__(self, arena, robot, mode_affichage=True):
        self.arena = arena
        self.robot = robot
        self.mode_affichage = mode_affichage
        
        if self.mode_affichage:
            self.root = tk.Tk()
            self.root.title("Simulation Robot")
            self.canvas = tk.Canvas(self.root, width=self.arena.width, height=self.arena.height, bg="white")
            self.canvas.pack()
            self.draw_arena()
        
    def draw_arena(self):
        """Dessine l'arène et les obstacles."""
        for obstacle in self.arena.obstacles:
            self.canvas.create_oval(
                obstacle.x - obstacle.radius, obstacle.y - obstacle.radius,
                obstacle.x + obstacle.radius, obstacle.y + obstacle.radius,
                fill="red"
            )
        self.robot_id = self.canvas.create_oval(
            self.robot.x - 5, self.robot.y - 5, self.robot.x + 5, self.robot.y + 5,
            fill="blue"
        )
    
    def update(self):
        """Met à jour l'affichage du robot."""
        update_affichage(self.canvas, self.robot_id, self.robot, self.mode_affichage)

    def run(self):
        if self.mode_affichage:
            self.root.mainloop()
