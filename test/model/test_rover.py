import unittest
from model.Rover import Rover
from model.Plateau import Plateau

ROVER_NAME = 'rover1'

class TestingRover(unittest.TestCase):

    def setUp(self):
        self._rover = Rover(ROVER_NAME)
        self._plateau = Plateau(5, 5)

    def test_landing_successful(self):
        expected_x, exptected_y = 1, 5
        direction = 'N'
        self._rover.land(self._plateau , expected_x, exptected_y, direction)
        self.assertEqual(expected_x, self._rover._x_position)
        self.assertEqual(exptected_y, self._rover._y_position)
        self.assertEqual(ROVER_NAME + ':1 5 N', self._rover.get_position_and_direction())

    def test_landing_invalid_position(self):
        with self.assertRaises(Exception):
            self._rover.land(self._plateau, 6, 7)

    def test_making_right_moves(self):
        expected_x, exptected_y = 1, 5
        direction = 'N'
        self._rover.land(self._plateau , expected_x, exptected_y, direction)
        self._rover.send_move_instructions(['L','M','L''M','L','M','L','R''M'])
        self.assertEqual(ROVER_NAME + ':0 4 E', self._rover.get_position_and_direction())


    def test_move_out_of_bound(self):
        expected_x, exptected_y = 1, 5
        direction = 'N'
        self._rover.land(self._plateau , expected_x, exptected_y, direction)
        with self.assertRaises(Exception):
            self._rover.send_move_instructions(['L', 'M', 'M''M', 'M', 'M', 'M', 'M''M'])


if __name__ == '__main__':
    unittest.main()
