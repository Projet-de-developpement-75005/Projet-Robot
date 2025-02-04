import pygame
import time
import math 
from robot import Voiture
from environnement import Environnement
from interface import Interface, VOITURE_LONGUEUR, VOITURE_LARGEUR


class EnvRobot:
    def __init__(self, robot, environment):
        self.robot = robot
        self.environment = environment

    