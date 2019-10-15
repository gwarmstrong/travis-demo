import nicole_task
import unittest


class TestNicoleTask(unittest.TestCase):

    def test_odd_number(self):
        a = 7
        exp = False
        obs = nicole_task.if_even_odd(a)
        self.assertEqual(exp, obs)

    def test_even_number(self):
        a = 2
        exp = True
        obs = nicole_task.if_even_odd(a)
        self.assertEqual(exp, obs)


if __name__ == '__main__':
    unittest.main()
