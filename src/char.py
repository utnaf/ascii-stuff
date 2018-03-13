import random


class Char:
    GREYSCALE_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    MAX_LEN = len(GREYSCALE_CHARS)

    def __init__(self, level=0):
        self._level = level

    def __repr__(self):
        return self.GREYSCALE_CHARS[self._level]
