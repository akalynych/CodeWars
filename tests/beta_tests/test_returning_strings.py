import unittest

from katas.beta.returning_strings import greet


class GreetTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(greet('Ryan'),
                         'Hello, Ryan how are you doing today?')

    def test_equals_2(self):
        self.assertEqual(greet('Zebulan'),
                         'Hello, Zebulan how are you doing today?')
