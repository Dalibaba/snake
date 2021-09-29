"""
Player class
"""
import constants


class Player:
    """
    Create Player with name and score
    """

    def __init__(self, name):
        self.name = name
        self.score = 0

    def increase_score(self):
        self.score = self.score + constants.Scoring.FOOD

    def reset(self):
        self.score = 0
