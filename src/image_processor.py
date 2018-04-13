import time
import sys
import io
import urllib.request
from src import *
from PIL import Image
from PIL import ImageStat
from pprint import pprint
from math import ceil


def to_ascii(image, screen, options):
    count = 0

    image_height, image_width = image.size
    range_x, range_y = screen.size

    result_string = ''

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
            result_string = result_string + str(Char(int(val), rgb, options.to_grayscale(), options.to_html()))

        if x < range_x:
            result_string = result_string + '\n'

    return result_string

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


def get_from_file(file):
    infile = file
    fileobject = Image.open(infile).convert('RGB')

    return fileobject

def get_from_url(url):
    with urllib.request.urlopen(url) as readed_url:
        return get_from_file(io.BytesIO(readed_url.read()))

    
