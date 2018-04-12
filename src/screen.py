import os

class Screen:
    def __init__(self, size):
        self.size = map(lambda num: int(num), size)
