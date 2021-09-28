"""
Food class
"""
import constants
import random


class Food:
    """
    Create Food with starting position and direction
    """

    def __init__(self, world_width, world_height, size_x=10, size_y=10):
        self.world_width = world_width
        self.world_height = world_height
        self.x, self.y = self.random_position(self.world_width, self.world_height)
        self.color = (30, 30, 100)
        self.size_x = size_x
        self.size_y = size_y

    def change_position(self):
        self.x, self.y = self.random_position(self.world_width, self.world_height)

    @staticmethod
    def random_position(world_width, world_height):
        x_pos = round(random.randint(0, world_width) / 10) * 10
        y_pos = round(random.randint(0, world_height) / 10) * 10
        return x_pos, y_pos
