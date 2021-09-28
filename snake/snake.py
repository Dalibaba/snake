"""
Snake class
"""
import constants
import random

directions = ["UP", "RIGHT", "DOWN", "LEFT"]


class Snake:
    """
    Create Snake with starting position and direction
    """

    def __init__(self, world_width, world_height, size_x=10, size_y=10):
        self.x = world_width / 2
        self.y = world_height / 2
        self.color = (0, 0, 0)
        self.size_x = size_x
        self.size_y = size_y
        self.direction = self.random_direction()
        self.length = 1
        self.block_positions = [[self.x,self.y]]

    def move(self, dx=10, dy=10):

        if self.direction == "UP":
            self.y = self.y - dy
        if self.direction == "DOWN":
            self.y = self.y + dy
        if self.direction == "RIGHT":
            self.x = self.x + dx
        if self.direction == "LEFT":
            self.x = self.x - dx

        # add newest position on "head" position
        self.block_positions.insert(0, [self.x, self.y])
        # delete latest position
        self.block_positions.pop()
    def turn(self, turn_direction):

        if turn_direction == "UP" and (self.direction == "RIGHT" or self.direction == "LEFT"):
            self.direction = turn_direction
        if turn_direction == "DOWN" and (self.direction == "RIGHT" or self.direction == "LEFT"):
            self.direction = turn_direction
        if turn_direction == "RIGHT" and (self.direction == "UP" or self.direction == "DOWN"):
            self.direction = turn_direction
        if turn_direction == "LEFT" and (self.direction == "UP" or self.direction == "DOWN"):
            self.direction = turn_direction

    def eat(self, ):
        self.length += 1
        # create new block on "head" position
        self.block_positions.insert(0, [self.x, self.y])

    @staticmethod
    def random_direction():
        return directions[random.randint(0, 3)]
