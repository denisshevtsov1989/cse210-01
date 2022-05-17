import random

"""
# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class declaration:
    def declaration_fundtion(number_cube_side):
        number_cube_side.random(1, 7)
        print(number_cube_side)

        # return
"""


class Die_game():

    def __init__(self):
        self.value = 0
        self.points = 0

    def first_game_function(self, number_cube_side):
        number_cube_side.random(1, 7)
        print(number_cube_side)
        return


"""A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for
    it.

    Attributes:
        value(int): The number of spots on the side facing up.
        points(int): The number of points the die is worth.
    """


# 2) Create the class constructor. Use the following method comment.
"""Constructs a new instance of Die with a value and points attribute.

       Args:
            self(Die): An instance of Die.
        """

# 3) Create the roll(self) method. Use the following method comment.
"""Generates a new random value and calculates the points.

        Args:
            self(Die): An instance of Die.
"""
