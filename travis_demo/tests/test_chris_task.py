from travis_demo import chris_task
import unittest


class TestChrisTask(unittest.TestCase):

    def test_no_input(self):
        self.assertEqual(chris_task.hello_world(), 'Hello world!')

    def test_empty_input(self):
        self.assertEqual(chris_task.hello_world(''), 'Hello world!')

    def test_normal_name(self):
        self.assertEqual(chris_task.hello_world('Chris'), 'Hello Chris!')

    def test_upper_name(self):
        self.assertEqual(chris_task.hello_world('CHRIS'), 'Hello Chris!')

    def test_lower_name(self):
        self.assertEqual(chris_task.hello_world('chris'), 'Hello Chris!')


if __name__ == '__main__':
    unittest.main()
