import time
import sys
import os
import io
import urllib.request
import argparse
from src import *
from PIL import Image
from PIL import ImageStat
from pprint import pprint
from math import ceil


def main(image, is_grayscale):
    count = 0
    screen = Screen()

    image_height, image_width = image.size
    range_x, range_y = screen.size

    if image_height > range_x:
        height_ratio = (image_height / range_x)
    else:
        height_ratio = 1
        range_y = image_height

    if image_width > range_y:
        width_ratio = (image_width / range_y)
    else:
        width_ratio = 1
        range_y = image_height

    for y in range(range_y):
        for x in range(range_x):
            tuple_dim = (int(height_ratio * x), int(width_ratio * y),
                         int(height_ratio * x + height_ratio), int(width_ratio * y + width_ratio))

            image_square = image.crop(tuple_dim)

            rgb = get_medium_color(image_square)

            square_stats = ImageStat.Stat(image_square)

            val = ((square_stats.mean[0] +
                    square_stats.mean[1]) / 2) % Char.MAX_LEN
            sys.stdout.write(str(Char(int(val), rgb[0], is_grayscale)))

        if x < range_x:
            sys.stdout.write('\n')


def get_medium_color(image):
    count = 1
    width, height = image.size

    red_amount = 0
    green_amount = 0
    blue_amount = 0

    for x in range(width):
        for y in range(height):
            count += 1
            r, g, b = image.getpixel((x, y))
            red_amount += r
            green_amount += g
            blue_amount += b

    return rgb2short(
        format(int(red_amount/count), '2x') +
        format(int(green_amount/count), '2x') +
        format(int(blue_amount/count), '2x')
    )


def get_image(file, url):
    infile = file
    if infile == None:
        with urllib.request.urlopen(url) as readed_url:
            infile = io.BytesIO(readed_url.read())

    fileobject = Image.open(infile).convert('RGB')

    return fileobject


parser = argparse.ArgumentParser(description="Convert an image into ASCII art")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", help="Local file path")
group.add_argument("-u", help="Remote url")

parser.add_argument("-g", help="Show the image in grayscale", action='store_true')
args = parser.parse_args()

try:
    main(get_image(args.f, args.u), args.g)
    input()
except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
