from .Plateau import Plateau
from constants import INSTRUCTION_LEFT_TURN, INSTRUCTION_RIGHT_TURN, INSTRUCTION_MOVE, NORTH, WEST, SOUTH, EAST


_DIRECTIONS_TURN_LEFT = {NORTH: WEST, SOUTH: EAST, WEST: SOUTH, EAST: NORTH}
_DIRECTIONS_TURN_RIGHT = {NORTH: EAST, SOUTH: WEST, WEST: NORTH, EAST: SOUTH}
_DELTA =  {NORTH: (0, 1), SOUTH: (0, -1), WEST: (-1, 0), EAST: (1, 0)}

class Direction:

    def __init__(self, symbol):
        if symbol not in _DIRECTIONS_TURN_LEFT.keys():
            raise Exception('invalid direction {}'.format(symbol))
        self._symbol = symbol

    def left(self):
        return Direction(_DIRECTIONS_TURN_LEFT[self._symbol])

    def right(self):
        return Direction(_DIRECTIONS_TURN_RIGHT[self._symbol])

    def delta(self):
        return _DELTA[self._symbol]

    def __repr__(self):
        return self._symbol

class Rover:

    def __init__(self, name):
        self._name = name
        self._plateau = None
        self._x_position = None
        self._y_position = None
        self._direction = None

    def land(self, plateau: Plateau, landing_x: int, landing_y: int, direction : str):
        if not plateau.is_valid_position(landing_x, landing_y):
            raise Exception("Not able to land because of valid landing for {}, {}".format(landing_x, landing_y))
        self._plateau = plateau
        self._x_position = landing_x
        self._y_position = landing_y
        self._direction = Direction(direction)

    def _left_turn(self):
        self._direction = self._direction.left()

    def _right_turn(self):
        self._direction = self._direction.right()

    def _move(self):
        delta_x, delta_y = self._direction.delta()
        proposed_move_x, proposed_move_y = self._x_position + delta_x, self._y_position + delta_y
        if not self._plateau.is_valid_position(proposed_move_x, proposed_move_y):
            raise Exception("Not able to make the move because of valid landing for {}, {}".format(proposed_move_x, proposed_move_y))
        self._x_position = proposed_move_x
        self._y_position = proposed_move_y

    def send_move_instructions(self, instructions):
        for instruction in instructions:
            if instruction is INSTRUCTION_LEFT_TURN:
                self._left_turn()
            elif instruction is INSTRUCTION_RIGHT_TURN:
                self._right_turn()
            elif instruction is INSTRUCTION_MOVE:
                self._move()

    def get_position_and_direction(self):
        return '{}:{} {} {}'.format(self._name, self._x_position, self._y_position, self._direction)

