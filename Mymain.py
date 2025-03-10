import tkinter as tk
from Simulation import EnvRobot

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulation Robot")
        self.canvas = tk.Canvas(self.root, width=900, height=800, bg="white")
        self.canvas.pack()

        print("Choisissez un mode :")
        print("1 - Mode Carré (le robot se déplace automatiquement en carré)")
        print("2 - Mode Classique (contrôle au clavier ou avec des vitesses)")
        choix = input("Entrez 1 ou 2 : ")

        self.simulation = EnvRobot(self.canvas, mode=int(choix))

    def run(self):
        self.simulation.demarrer_simulation()
        self.root.mainloop()

if __name__ == "__main__":
    app = Main()
    app.run()