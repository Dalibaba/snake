"""
database class
"""

from tinydb import TinyDB


class database:

    def __init__(self):
        self.db = TinyDB('db.json')

    def insert(self, player_name, player_score):
        self.db.insert({'name': player_name, 'score': player_score})

    def get_highscore(self, ):
        highscore = self.db.all()
        highscore.sort(key=lambda k: k['score'])
        highscore.reverse()
        print(highscore)
        return highscore[:10]
