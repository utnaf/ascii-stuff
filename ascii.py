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

    # pprint((height_ratio, width_ratio, range_x, range_y, screen.size))
    # exit()

    for y in range(range_y):
        for x in range(range_x):
            tuple_dim = (int(height_ratio * x), int(width_ratio * y),
                         int(height_ratio * x + height_ratio), int(width_ratio * y + width_ratio))

            # pprint(tuple_dim);
            image_square = image.crop(tuple_dim)

            square_stats = ImageStat.Stat(image_square)

            val = ((square_stats.mean[0] +
                    square_stats.mean[1]) / 2) % Char.MAX_LEN
            sys.stdout.write(str(Char(int(val))))

        if x < range_x:
            sys.stdout.write('\n')


def get_image():
    infile = sys.argv[1]

    if infile == None:
        exit('Error')

    fileobject = Image.open(infile).convert('LA')

    return fileobject


try:
    main(get_image())
    input()
except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
