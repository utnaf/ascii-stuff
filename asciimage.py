#! /usr/bin/env python

__author__ = 'Davide Effe utnaf.dev@gmail.com'
__version__ = '0.1'
__license__ = 'WTFPL http://sam.zoy.org/wtfpl/'

#---------------------------------------------------------------------

from src import to_ascii
from src import Screen
from src import Options
from src import get_from_file
from src import get_from_url

if __name__ == '__main__':
    import argparse
    import sys
    import os
    from src import FileWriter

    parser = argparse.ArgumentParser(
        description="Convert an image into ASCII art")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", help="Local file path")
    group.add_argument("-u", help="Remote url")

    parser.add_argument(
        "-g", help="Show the image in grayscale", action='store_true')
    parser.add_argument(
        "-w", help="To HTML", action="store_true")

    args = parser.parse_args()

    options = Options(args)

    image = None
    if args.f:
        image = get_from_file(args.f)
    else:
        image = get_from_url(args.u)

    y, x = os.popen('stty size', 'r').read().split()
    output = to_ascii(image, Screen((x, y)), options)

    writer = FileWriter(options.to_html())
    writer.write(output)
