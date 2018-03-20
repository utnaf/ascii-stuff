import random


class Char:
    GREYSCALE_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    MAX_LEN = len(GREYSCALE_CHARS)

    def __init__(self, level, color):
        self._level = level
        self._color = color

    def __repr__(self):
        
        return '\x1b[38;5;' + self._color + 'm' + self.GREYSCALE_CHARS[self._level]
