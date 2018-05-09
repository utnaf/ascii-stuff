import random


class Char:
    GREYSCALE_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    MAX_LEN = len(GREYSCALE_CHARS)

    def __init__(self, level, color, is_greyscale, is_terminal):
        self._level = level
        self._color = color
        self._is_greyscale = is_greyscale
        self.is_terminal = is_terminal

    def __repr__(self):
        if self.is_terminal:
            return self.to_shell()
        else:
            return self.to_html()

    def to_html(self):
        if self._is_greyscale:
            return '<span>' + self.GREYSCALE_CHARS[self._level] + '</span>'
        else:
            return '<span style="color: #' + self._color[1] + '">' + self.GREYSCALE_CHARS[self._level] + '</span>'

    def to_shell(self):
        if self._is_greyscale:
            return self.GREYSCALE_CHARS[self._level]
        else:
            return '\x1b[38;5;' + self._color[0] + 'm' + self.GREYSCALE_CHARS[self._level]
