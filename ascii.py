import time
import sys
import os
from src import *
from PIL import Image
from PIL import ImageStat
from pprint import pprint
from math import ceil


def main(image):
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
            sys.stdout.write(str(Char(int(val), rgb[0])))

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


def get_image():
    infile = sys.argv[1]

    if infile == None:
        exit('Error')

    fileobject = Image.open(infile).convert('RGB')

    return fileobject


try:
    main(get_image())
    input()
except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
