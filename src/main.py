import tkinter as tk
from Simulation import EnvRobot

class Main:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Simulation Robot")
        self.canvas = tk.Canvas(self.root, width=900, height=800, bg="white")
        self.canvas.pack()

    def run(self):
        self.simulation.demarrer_simulation()

if __name__ == "__main__":
    app = Main()
    app.run()
