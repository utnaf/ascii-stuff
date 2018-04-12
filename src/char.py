import random


class Char:
    GREYSCALE_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    MAX_LEN = len(GREYSCALE_CHARS)

    def __init__(self, level, color, is_greyscale, is_html):
        self._level = level
        self._color = color
        self._is_greyscale = is_greyscale
        self._is_html = is_html

    def __repr__(self):
        if self._is_html:
            return self.to_html()
        else:
            return self.to_shell()

    def to_html(self):
        if self._is_greyscale:
            return '<span style="font-face: mono">' + self.GREYSCALE_CHARS[self._level] + '</span>'
        else:
            return '<span style="font-face: mono; color: #' + self._color[1] + '">' + self.GREYSCALE_CHARS[self._level] + '</span>'

    def to_shell(self):
        if self._is_greyscale:
            return self.GREYSCALE_CHARS[self._level]
        else:
            return '\x1b[38;5;' + self._color[0] + 'm' + self.GREYSCALE_CHARS[self._level]
