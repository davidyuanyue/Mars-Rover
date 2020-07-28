import unittest

from mars_rover_entry_point import *

class TestingMarsRover(unittest.TestCase):

    def test_get_subfix_after_pattern(self):
        text = "111:abc:222"
        pattern = ":abc:"
        bad_pattern = "kkkk"
        self.assertEqual("222",get_subfix_after_pattern(text, pattern))
        self.assertEqual("", get_subfix_after_pattern(text, bad_pattern))

    def test_get_prefix_before_pattern(self):
        text = "111:abc:222"
        pattern = ":abc:"
        bad_pattern = "kkkk"
        self.assertEqual("111",get_prefix_before_pattern(text, pattern))
        self.assertEqual("111:abc:222", get_prefix_before_pattern(text, bad_pattern))

    def test_parse_upper_right_limit(self):
        text = 'Plateau:6 7'
        positions = parse_upper_right_limit(text)
        self.assertTupleEqual((6, 7), positions)

    def test_parse_landing(self):
        text = 'Rover1 Landing:5 6 N'
        x, y, direction = parse_landing(text)
        self.assertEqual(5, x)
        self.assertEqual(6, y)
        self.assertEqual("N", direction)

    def test_parse_rover_name(self):
        text = 'Rover1 Landing:5 6 N'
        rover_name = parse_rover_name(text)
        self.assertEqual('Rover1', rover_name)

    def test_parse_instructions(self):
        text = 'Rover1 Instructions:LMLMLMLMM'
        instructions = parse_instructions(text)
        self.assertListEqual(['L','M','L','M','L','M','L','M','M'], instructions)
