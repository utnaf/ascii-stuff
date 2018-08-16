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

    args = parser.parse_args()
    image = None
    if args.l:
        image = asciimage.get_from_path(args.l)
    else:
        image = asciimage.get_from_url(args.u)

    output = asciimage.to_ascii(image, pixel_size=5)

    writer = asciimage.FileWriter()
    writer.write(output)

try:
    main()
except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
