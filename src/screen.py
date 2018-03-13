import os

class Screen:
    def __init__(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.size = (int(columns), int(rows))
