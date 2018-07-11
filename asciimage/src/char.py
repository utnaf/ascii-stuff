import random


class Char:
    def __init__(self, color):
        self._color = color

    def __repr__(self):
        return self.to_html()

    def to_html(self):
        return '<span style="color: #' + self._color + '">#</span>'
