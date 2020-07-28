import sys
from model.Plateau import Plateau
from model.Rover import Rover
from constants import *


def get_subfix_after_pattern(text, pattern):
    return text.partition(pattern)[2]

def get_prefix_before_pattern(text, pattern):
    return text.partition(pattern)[0]

def parse_upper_right_limit(input_line):
    coordinates = get_subfix_after_pattern(input_line, INPUT_PATTERN_UPPER_RIGHT_POSITION)
    coordinates_list = coordinates.split()
    if len(coordinates_list) != 2:
        raise Exception('invalid upper right limit :{}'.format(input_line))
    return tuple(int(coordinate) for coordinate in coordinates_list)

def parse_landing(input_line):
    landing_info = get_subfix_after_pattern(input_line, INPUT_PATTERN_LANDING_POSITION)
    landing_info_list = landing_info.split()
    if len(landing_info_list) != 3:
        raise Exception('invalid landing :{}'.format(input_line))
    return int(landing_info_list[0]), int(landing_info_list[1]), landing_info_list[2]

def parse_rover_name(input_line):
    name = get_prefix_before_pattern(input_line, INPUT_PATTERN_LANDING_POSITION)
    return name.strip()

def parse_instructions(input_line):
    instructions = get_subfix_after_pattern(input_line, INPUT_PATTERN_INSTRUCTION)
    return [instruction for instruction in instructions]

def setup_plateau(input_line):
    x, y = parse_upper_right_limit(input_line)
    return Plateau(x, y)

plateau = None
rover = None

if __name__ == '__main__':
    for line in sys.stdin:
        input_line = line.strip('\n').strip()

        if len(input_line) == 0:
            continue
        if INPUT_PATTERN_UPPER_RIGHT_POSITION in input_line:
            plateau = setup_plateau(input_line)
        elif INPUT_PATTERN_LANDING_POSITION in input_line:
            x, y, direction = parse_landing(input_line)
            rover_name = parse_rover_name(input_line)
            rover = Rover(rover_name)
            rover.land(plateau, x, y, direction)
        elif INPUT_PATTERN_INSTRUCTION in input_line:
            instructions = parse_instructions(input_line)
            rover.send_move_instructions(instructions)
            print(rover.get_position_and_direction())
        else:
            print("invalid input line")
