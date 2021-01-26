import numpy as np

class Board():
    def __init__(self, length: int = 800, square_number: int = 8):
        self.board_length = length
        self.board_square_number = square_number
        self.square_size = self.board_length / self.board_square_number

        #The field with all parameters
        self.field = np.zeros(shape=(8,8), dtype=[('name', 'U2'), ('x', int), ('y', int), ('occupied', bool), ('piece', 'U15')])

        #Fill the names in the field array from a1 to h8
        for x, char in enumerate(self.char_range('A', 'H')):
            for y, number in enumerate(range(8, 0, -1)):
                self.field['name'][y][x] = f"{char}{number}"

        print(self.field['name'])

        #Fill the coordinates
        for x in range(8):
            for y in range(8):
                self.field['x'][y][x] = x * self.square_size
                self.field['y'][y][x] = y * self.square_size


        # print(f"{self.field['x']}\n{self.field['y']}")



    def char_range(self, c1, c2):
        """Generates the characters from `c1` to `c2`."""
        for c in range(ord(c1), ord(c2) + 1):
            yield chr(c)