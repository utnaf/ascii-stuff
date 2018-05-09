#! /usr/bin/env python

import asciimage
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(
        description="Convert an image into ASCII art")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", help="Local file path")
    group.add_argument("-u", help="Remote image url")

    parser.add_argument(
        "-g", help="Show the image in grayscale", action='store_true')
    parser.add_argument(
        "-t", help="To terminal", action="store_true")

    args = parser.parse_args()
    image = None
    if args.l:
        image = asciimage.get_from_file(args.l)
    else:
        image = asciimage.get_from_url(args.u)

    dims = None
    if args.t == True:
        y, x = os.popen('stty size', 'r').read().split()
        dims = (int(x), int(y))

    output = asciimage.to_ascii(image, dims, args.g, args.t, pixel_size=10)

    writer = asciimage.FileWriter(args.t)
    writer.write(output)

try:
    main()
except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
