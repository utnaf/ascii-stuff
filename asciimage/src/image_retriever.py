from io import BytesIO
from urllib import request
from PIL import Image

def get_from_path(filepath):
    fileobject = Image.open(filepath).convert("RGB")

    return fileobject

def get_from_url(url):
    with request.urlopen(url) as readed_url:
        return get_from_path(BytesIO(readed_url.read()))
