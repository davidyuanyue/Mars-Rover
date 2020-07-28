class Plateau:

    def __init__(self, x_limit, y_limit):
        self.x_limit = x_limit
        self.y_limit = y_limit

    def is_valid_position(self, x, y):
        if x >=0 and x <= self.x_limit and y >=0 and y<= self.y_limit:
            return True
        else:
            return False
