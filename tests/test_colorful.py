import unittest
from colorful import Colorful

class MachineTest(unittest.TestCase):
    def test_two_digits_is_colorful(self):
        c = Colorful()
        result = c.is_colorful(25)
        self.assertIs(result, True)

    def test_two_digits_is_not_colorful(self):
        c = Colorful()
        result = c.is_colorful(11)
        self.assertIs(result, False)

    def test_is_colorful(self):
        c = Colorful()
        result = c.is_colorful(263)
        self.assertIs(result, True)

    def test_is_not_colorful(self):
        c = Colorful()
        result = c.is_colorful(236)
        self.assertIs(result, False)
