import unittest
from travis_demo import nicole_task
import numpy as np


class TestTask(unittest.TestCase):

    def test_odd_number(self):
        a = 7
        exp = False
        obs = nicole_task.ifEvenOdd(a)
        self.assertEquals(exp, obs)

    def test_even_number(self):
        a = 2
        exp = True
        obs = nicole_task.ifEvenOdd(a)
        self.assertEquals(exp, obs)
