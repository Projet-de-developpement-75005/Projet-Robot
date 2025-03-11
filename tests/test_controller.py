import unittest
from unittest.mock import MagicMock
from controller.controller import Deplacement, CapteurDistance, DessinerCarre, Controller

class TestDeplacement(unittest.TestCase):
    def setUp(self):
        self.robot = MagicMock()
        self.deplacement = Deplacement(self.robot)

    def test_deplacer(self):
        self.robot.direction = 0  # robot regarde vers l'est
        self.deplacement.deplacer(10)
        self.assertEqual(self.robot.x, 10)
        self.assertEqual(self.robot.y, 0)

    def test_tourner(self):
        self.deplacement.tourner(90)
        self.assertEqual(self.robot.direction, 90)
        self.deplacement.tourner(270)  # tourne à gauche pour revenir à 0
        self.assertEqual(self.robot.direction, 0)
