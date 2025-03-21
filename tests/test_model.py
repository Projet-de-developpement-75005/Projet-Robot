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

    def test_obstacle(self):
        obstacle = Obstacle(10, 10, 5)
        self.assertEqual(obstacle.x, 10)
        self.assertEqual(obstacle.y, 10)
        self.assertEqual(obstacle.radius, 5)
    
    def test_robot(self):
        robot = Robot(5, 5, 90)
        self.assertEqual(robot.x, 5)
        self.assertEqual(robot.y, 5)
        self.assertEqual(robot.direction, 90)

    def test_update_model(self):
        arena = Arena()
        robot = Robot()
        obstacle = Obstacle(0, 0, 1)
        arena.add_obstacle(obstacle)
        update_model(arena, robot)