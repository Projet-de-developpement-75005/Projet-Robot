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


