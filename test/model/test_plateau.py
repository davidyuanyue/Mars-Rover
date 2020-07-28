
import unittest
from model.Plateau import Plateau


class TestingRover(unittest.TestCase):

    def setUp(self):
        self._plateau = Plateau(5, 5)


    def test_valid_position(self):
        self.assertTrue(self._plateau.is_valid_position(0, 0))
        self.assertTrue(self._plateau.is_valid_position(0, 5))
        self.assertTrue(self._plateau.is_valid_position(2, 1))
        self.assertTrue(self._plateau.is_valid_position(5,5))
        self.assertFalse(self._plateau.is_valid_position(5,6))
        self.assertFalse(self._plateau.is_valid_position(5,-1))