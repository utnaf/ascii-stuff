from io import BytesIO
from urllib import request
from PIL import Image, ImageStat
from math import ceil
from .colortrans import rgb2short
from .char import Char
from pprint import pprint

def normalize_image(image, max_dims, pixel_size):
    image_height, image_width = image.size
    ratio = image_height / image_width

    if image_height > image_width:
        new_image_width = int(max_dims[1] * pixel_size)
        new_image_height = int(new_image_width / ratio)
    else:
        new_image_height = int(max_dims[0] * pixel_size)
        new_image_width = int(new_image_height / ratio)

    return image.resize((new_image_width, new_image_height), Image.NEAREST)

def to_ascii(raw_image, max_dims = None, greyscale = False, to_html = False, pixel_size=5):
    if max_dims == None:
        max_dims = (200, 150)

    max_dims = (int(max_dims[0]),int(max_dims[1]), pixel_size)
    image = normalize_image(raw_image, max_dims)
    raw_image.close()
    image_height, image_width = image.size

    result_string = ''

    range_x = int(image_height / pixel_size)
    range_y = int(image_width / pixel_size)

    for y in range(range_y):
        for x in range(range_x):
            tuple_dim = (int(pixel_size * x), int(pixel_size * y),
                         int(pixel_size * x + pixel_size), int(pixel_size * y + pixel_size))

            image_square = image.crop(tuple_dim)

            rgb = get_medium_color(image_square)

            square_stats = ImageStat.Stat(image_square)
            image_square.close()

            val = ((square_stats.mean[0] +
                    square_stats.mean[1]) / 2) % Char.MAX_LEN
            result_string = result_string + str(Char(int(val), rgb, greyscale, to_html))

        if x < range_x:
            result_string = result_string + '\n'

    image.close()

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

    
