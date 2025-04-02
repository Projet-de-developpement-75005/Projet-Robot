# view/view_3d.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

class View3D:
    def __init__(self, arene, robot):
        self.arene = arene
        self.robot = robot
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.trace = []

    def draw_robot(self):
        self.ax.clear()
        self.ax.set_xlim(0, self.arene.largeur)
        self.ax.set_ylim(0, self.arene.hauteur)
        self.ax.set_zlim(0, 100)  # Hauteur fictive

        # Dessiner obstacles
        for obs in self.arene.obstacles:
            self.ax.bar3d(obs.x, obs.y, 0, obs.largeur, obs.hauteur, 50, color='red', alpha=0.5)

        # Dessiner robot
        self.ax.scatter(self.robot.x, self.robot.y, 10, color='blue', s=100)

        # Tracer trajectoire
        if self.trace:
            xs, ys = zip(*self.trace)
            zs = [10] * len(xs)
            self.ax.plot(xs, ys, zs, color='green')

        plt.draw()
        plt.pause(0.01)

    def run_simulation(self, controller, strategie, dt):
        strategie.start(controller.adapter)
    
        while not strategie.update(controller.adapter, dt):
            if not plt.fignum_exists(self.fig.number):
                print("Fenêtre fermée par l'utilisateur.")
                break  # Sort de la boucle si la fenêtre a été fermée

            self.trace.append((self.robot.x, self.robot.y))
            self.draw_robot()
            time.sleep(dt)

        strategie.stop(controller.adapter)
        print("Stratégie terminée.")
        plt.close(self.fig)  # Ferme proprement la figure s'il reste quelque chose
