import random


class Char:
    TYPE_NEUTRAL = 0
    TYPE_DARK = 1
    TYPE_LIGHT = 2

    CHARS = [
        ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5']
    ]

    def __init__(self, type=None):
        if type == None:
            type = self.TYPE_NEUTRAL
        self.type = type

    def __repr__(self):
        return random.choice(self.CHARS[self.type])
