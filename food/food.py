"""
Food class
"""

import random


class Food:

    """
    Create Food with starting position and direction
    """

    def __init__(self, world_min_x, world_max_x, world_min_y, world_max_y, size_x=10, size_y=10):
        self.world_min_x = world_min_x
        self.world_max_x = world_max_x - 10
        self.world_min_y = world_min_y
        self.world_max_y = world_max_y - 10

        self.x, self.y = self.random_position(self.world_min_x, self.world_max_x, self.world_min_y, self.world_max_y)
        self.color = (30, 30, 100)
        self.size_x = size_x
        self.size_y = size_y

    def change_position(self):
        self.x, self.y = self.random_position(self.world_min_x, self.world_max_x, self.world_min_y, self.world_max_y)

    @staticmethod
    def random_position(world_min_x, world_max_x, world_min_y, world_max_y):
        x_pos = (round(random.randint(world_min_x, world_max_x) / 10) * 10)
        y_pos = (round(random.randint(world_min_y, world_max_y) / 10) * 10)
        return x_pos, y_pos
