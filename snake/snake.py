"""
Snake class
"""
import constants
import random


directions = ["UP", "RIGHT", "DOWN", "LEFT"]

class Snake:
    """
    Create Snake with starting position
    """

    def __init__(self, world_width, world_height, size_x=10, size_y=10):
        self.x = world_width / 2
        self.y = world_height / 2
        self.color = (0, 0, 0)
        self.size_x = size_x
        self.size_y = size_y
        self.start_direction = self.random_direction()

    def move(self, dx=10, dy=10):
        self.x = self.x + dx
        self.y = dy + self.y

    @staticmethod
    def random_direction():
        return directions[random.randint(0, 3)]
