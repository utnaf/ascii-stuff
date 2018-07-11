from PIL import Image

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
