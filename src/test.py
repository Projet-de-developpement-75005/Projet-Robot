import unittest
from unittest.mock import MagicMock

from robot import Robot, Environment, EnvRobot

class TestRobotEnvironment(unittest.TestCase):
    def test_position_initiale(self):
        robot = Robot()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)
        self.assertEqual(robot.orientation, 0)

    def test_tourner(self):
        robot = Robot()
        robot.tourner(90)
        self.assertEqual(robot.orientation, 90)
        robot.tourner(-45)
        self.assertEqual(robot.orientation, 45)
        robot.tourner(360)
        self.assertEqual(robot.orientation, 45)

    def test_environment_position_valide(self):
        env = Environment(10, 10, [(2, 2), (4, 4)])
        self.assertTrue(env.est_valide_position(0, 0))
        self.assertFalse(env.est_valide_position(2, 2))
        self.assertFalse(env.est_valide_position(10, 10))
        self.assertTrue(env.est_valide_position(9, 9))

    


    

if _name_ == "_main_":
    unittest.main()
