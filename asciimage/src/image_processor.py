from io import BytesIO
from urllib import request
from PIL import Image, ImageStat
from math import ceil
from .colortrans import rgb2short
from .char import Char
from pprint import pprint

def normalize_image(image, max_dims):
    pixel_size = 5
    image_height, image_width = image.size
    ratio = image_height / image_width

    if image_height > image_width:
        new_image_width = int(max_dims[1] * pixel_size)
        new_image_height = int(new_image_width / ratio)
    else:
        new_image_height = int(max_dims[0] * pixel_size)
        new_image_width = int(new_image_height / ratio)

    return image.resize((new_image_width, new_image_height), Image.NEAREST)

def to_ascii(raw_image, max_dims = None, greyscale = False, to_html = False):
    if max_dims == None:
        max_dims = (103, 77)

    max_dims = (int(max_dims[0]),int(max_dims[1]))
    image = normalize_image(raw_image, max_dims)
    image_height, image_width = image.size
    range_x, range_y = max_dims

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
            result_string = result_string + str(Char(int(val), rgb, greyscale, to_html))

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
    with request.urlopen(url) as readed_url:
        return get_from_file(io.BytesIO(readed_url.read()))

    
