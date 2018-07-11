from PIL import Image, ImageStat
from math import ceil
from .colortrans import rgb2short
from .image_dimensions import normalize_image
from .char import Char
from pprint import pprint

def suggest_background(image):
    return "#" + get_medium_color(image)[1]

def to_ascii(raw_image, pixel_size=5):
    max_dims = (120, 120)

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

            square_colors = image.crop(tuple_dim).getcolors(8)

            fg_color = "#ffffff"
            if square_colors != None:
                fg_color = to_html_color(avg_color(square_colors))

            result_string = result_string + str(Char(fg_color))

        if x < range_x:
            result_string = result_string + '\n'

    image.close()

    return result_string

def avg_color(colors):
    color_sum_r = 0
    color_sum_g = 0
    color_sum_b = 0

    weight_sum = 0

    for color_tuple in colors:
        color_sum_r += color_tuple[0] * color_tuple[1][0]
        color_sum_g += color_tuple[0] * color_tuple[1][1]
        color_sum_b += color_tuple[0] * color_tuple[1][2]

        weight_sum += color_tuple[0]

    return (
        int(color_sum_r / weight_sum),
        int(color_sum_g / weight_sum),
        int(color_sum_b / weight_sum)
    )

def to_html_color(rgb_tuple):
    return format(rgb_tuple[0], '2x') + format(rgb_tuple[1], '2x') + format(rgb_tuple[2], '2x')
