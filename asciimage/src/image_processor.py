from io import BytesIO
from urllib import request
from PIL import Image, ImageStat
from math import ceil
from .colortrans import rgb2short
from .char import Char
from pprint import pprint

def decide_dimensions(image_dims, max_dims, pixel_size = 1):
    image_w, image_h = image_dims
    max_w, max_h = max_dims

    image_ratio = image_h / image_w

    if image_w > image_h and image_w > max_w and not max_w * image_ratio > max_h:
        new_image_w = max_w
        new_image_h = new_image_w * image_ratio
    elif image_h > max_h:
        new_image_h = max_h
        new_image_w = new_image_h / image_ratio
    else:
        new_image_w = image_w
        new_image_h = image_h

    return (int(new_image_w * pixel_size), int(new_image_h * pixel_size))

def normalize_image(image, max_dims, pixel_size):
    return image.resize(decide_dimensions(image.size, max_dims, pixel_size), Image.NEAREST)

def suggest_background(image):
    return "#" + get_medium_color(image)[1]

def to_ascii(raw_image, max_dims = None, greyscale = False, to_terminal = False, pixel_size=5, with_bg=True):
    if max_dims == None:
        max_dims = (100, 100)

    image = normalize_image(raw_image, max_dims, pixel_size)
    raw_image.close()
    image_width, image_height = image.size

    result_string = ''

    range_x = int(image_width / pixel_size)
    range_y = int(image_height / pixel_size)

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
            result_string = result_string + str(Char(int(val), rgb, greyscale, to_terminal))

        if x < range_x:
            result_string = result_string + '\n'

    suggested_background = "#fff"
    if with_bg:
        suggested_background = suggest_background(image);
    image.close()

    return (
        result_string,
        suggested_background
    )

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
        return get_from_file(BytesIO(readed_url.read()))

    
