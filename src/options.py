""" usage: asciimage.py [-h] (-f F | -u U) [-g] [-w] [-s S]

Convert an image into ASCII art

optional arguments:
  -h, --help  show this help message and exit
  -f F        Local file path
  -u U        Remote url
  -g          Show the image in grayscale
  -w          To HTML
  -s S        Save to file
"""

class Options:
    def __init__(self, args):
        self.args = args

    def to_html(self):
        return self.args.w == True

    def to_grayscale(self):
        return self.args.g == True
