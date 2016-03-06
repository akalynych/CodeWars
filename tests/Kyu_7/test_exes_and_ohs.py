import unittest

from Kyu_7.exes_and_ohs import xo


class XOTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(xo('xo'))

    def test_true_2(self):
        self.assertTrue(xo('xo0'))

    def test_false(self):
        self.assertFalse(xo('xxxoo'))


if __name__ == '__main__':
    unittest.main()
