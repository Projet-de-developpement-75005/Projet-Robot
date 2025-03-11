# tests/test_model.py
import unittest
from Model.arene import Arena
from Model.robot import Robot
from Model.obstacle import Obstacle
from Model.update_model import update_model

class TestModel(unittest.TestCase):
    def test_arena(self):
        arena = Arena(200, 200)
        self.assertEqual(arena.width, 200)
        self.assertEqual(arena.height, 200)